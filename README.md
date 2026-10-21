# Maspy Communication examples

Small playground for experimenting with MASPY communication acts between agents.

## Run

```bash
make setup
make run
```

`make help` lists all available commands.

## Experiments

### Messaging patterns

- [ ] Send/receive (unicast, one-to-one) — `achieve`
- [ ] Sample messages (multicast, one-to-many) — `achieve`, `tell`, `tellHow`
- [ ] Broadcast (one-to-all) — act not defined yet

### Communication acts not covered by the examples above

- [ ] `untell` (Belief)
- [ ] `untellHow` (Plan)
- [ ] `unachieve` (Goal)
- [ ] `askOne` / `askOneReply` (Ask)
- [ ] `askAll` / `askAllReply` (Ask)
- [ ] `askHow` (Ask)