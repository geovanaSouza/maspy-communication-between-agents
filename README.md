# Maspy Communication examples

Small playground for experimenting with MASPY communication acts between agents.

## Run

```bash
make setup
make run
```

To run against the MASPY `integration` branch:

```bash
make install-integration
make run
```

Use `make install-maspy MASPY="git+https://github.com/geovanaSouza/MASPY.git@<ref>"` to install another MASPY ref.

`make help` lists all available commands.

## Experiments

### Messaging patterns

- [x] Send/receive (unicast, one-to-one) — `achieve`
- [x] Sample messages (many-to-one) — `achieve`, `tellHow`
- [ ] Multicast (one-to-many) — `achieve`
- [ ] Broadcast (one-to-all) — act not defined yet

### Communication acts not covered by the examples above

- [ ] `tell` (Belief)
- [ ] `untell` (Belief)
- [ ] `untellHow` (Plan)
- [ ] `unachieve` (Goal)
- [ ] `askOne` / `askOneReply` (Ask)
- [ ] `askAll` / `askAllReply` (Ask)
- [ ] `askHow` (Ask)