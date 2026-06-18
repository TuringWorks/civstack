# Control and AI threat model

## Trust boundaries

The safety MCU and actuator network are trusted only for bounded deterministic
control. The local AI computer, language model, microphone, camera and any external
network are untrusted request sources. Safety does not depend on their correctness.

## Required controls

- Allowlisted, typed motion skills with range, rate, workspace and deadline checks.
- Authenticated controller updates and configuration hashes in test records.
- Network separation between actuator bus and general-purpose computer.
- No direct shell, torque, PWM or raw trajectory tool exposed to an LLM.
- Replay/stale-command rejection, monotonically increasing command IDs and watchdogs.
- Physical enable and hardwired E-stop override every software state.
- Default-deny remote access; no unattended external command channel.
- Logs are append-only during tests and contain command source and rejection reason.

## Abuse cases to test

Malformed values, prompt injection through perceived text/speech, repeated valid
commands, contradictory skills, network flood, stale replay, clock loss, brain-computer
crash, MCU reset and partial bus isolation. Every case must resolve to reject, hold or
controlled safe stop without defeating the hardware stop chain.

