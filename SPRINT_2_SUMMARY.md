# Sprint 2 — Summary

## Objective
The goal of Sprint 2 was to evolve the system from a manually stepped simulation into a robust, time-aware control system with autonomous execution, while preserving architectural clarity, correctness, and testability.

---

## Scope
Sprint 2 focused on:
- Time-based command scheduling
- Temporal correctness of command effects
- Autonomous background execution
- Minimal but effective thread-safety
- Clear separation between control, execution, and domain logic

Out of scope:
- Persistent storage
- Real-time guarantees
- Advanced observability and metrics
- Production-grade concurrency handling

---

## Implemented features

### Command queue and durations
- Introduction of a command model with explicit execution duration
- Command queue managed at the application layer
- Commands persist across multiple simulation steps
- Support for overlapping commands

### Temporal correctness
- Command effects scaled proportionally to the actual time applied within each step
- Correct aggregation of forces and torques for partial durations
- Deterministic temporal integration
- Test coverage validating time scaling and overlap behavior

### Background simulation execution
- Introduction of a background simulation runner using a dedicated thread
- Automatic periodic execution of simulation steps
- Explicit lifecycle controls: start, pause, resume, stop
- Separation of execution infrastructure from control logic

### Thread-safety and robustness
- Application-level locking to protect shared state
- Safe interaction between API requests and background execution
- Snapshot-based state exposure to avoid leaking internal references
- Safe reset handling while background execution is active

---

## Architecture overview

- **Domain**
  - Remains pure and free of execution or concurrency concerns

- **Application**
  - Owns command scheduling and temporal logic
  - Orchestrates simulation execution
  - Provides thread-safe access to shared state

- **Infrastructure**
  - Background execution loop
  - Thread-based simulation runner

- **API**
  - Control endpoints for simulation lifecycle
  - Safe, read-only exposure of runtime state

---

## Key technical decisions
- Explicit time integration over implicit accumulation
- Thread-based execution for simplicity and determinism
- Single lock strategy for correctness over performance
- Snapshot-based state exposure instead of raw object access
- Infrastructure introduced only when required

---

## Known limitations
- Background runner is not real-time accurate
- Thread-safety is minimal but sufficient for current scope
- All state remains in-memory
- No persistence or recovery mechanisms

These limitations are conscious trade-offs for this stage of the project.

---

## Current status
The system now supports:
- Manual and autonomous simulation execution
- Time-based command scheduling with durations
- Overlapping control inputs
- Safe concurrent access via API
- Clean lifecycle management

Sprint 2 successfully establishes a robust and extensible execution foundation.

---

## Next steps
Sprint 3 will focus on:
- State and history persistence
- Structured logging and observability
- Exporting telemetry and diagnostics
- Preparing the system for longer-running scenarios
