from maspy import *

class Sample(Agent):
    def on_idle(self):
        if self.has(Belief("sender")):
            return
        if self.saved_msgs:
            return
        if not Admin().running_class_agents("Sender"):
            self.stop_cycle()
    
    @pl(gain, Goal("print", Any))
    def print_plan(self, src, msg):
        self.print(f"Running the Agent {self.my_name} Plan, message: {msg}")

    def agents_with_belief(self, belief_name: str) -> list[str]:
        channel = self._channels["default"]
        return [
            name for name in self.list_agents("Sample")
            if any(b.name == belief_name for b in channel._agents[name].belief_list)
        ]

    @pl(gain, Goal("send_info", Any), Belief("sender"))
    def send_info(self, src, msg):
        msg = f"{msg} from {self.my_name}"
        for agent in self.agents_with_belief("receiver"):
            self.print(f"Sending message ({msg}) to {agent}")
            self.send(agent, achieve, Goal("receive_info", msg))
        self.stop_cycle()

    @pl(gain, Goal("receive_info", Any), Belief("receiver"))
    def receiver(self, src, msg):
        self.print(f"Information [{msg}] - Received from {src}")
        test_agents_list = self.list_agents("Test")
        for agent in test_agents_list:
            plan = self.get(Plan, Goal("print", Any))
            self.send(agent, tellHow, plan)
            self.send(agent, achieve, Goal("print", msg))

class Test(Agent):
    def add(self, data_type, instant=False, no_lock=False):
        super().add(data_type, instant, no_lock)

        # MASPY 2026.5.13 does not rebuild the plan index when a Plan is added.
        if isinstance(data_type, Plan):
            self._build_plan_index()

    def on_idle(self):
        if self.saved_msgs:
            return
        if Admin().running_class_agents("Receiver"):
            return
        if self.idle_counter < 2:
            return
        self.stop_cycle()

if __name__ == "__main__":
    print("Many-to-one example")

    Channel().show_exec = True

    for i in range(1, 5):
        sender = Sample("Sender", goals=Goal("send_info", "Hello"))
        sender.add(Belief("sender"))

    receiver = Sample("Receiver", Belief("receiver"))

    Test(read_all_mail=True)
    
    Admin().start_system()