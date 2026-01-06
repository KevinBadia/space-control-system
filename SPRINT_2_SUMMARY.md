# Sprint 2 — Summary

## Objective
The goal of Sprint 2 is to evolve the system from a manually stepped simulation into a more realistic and robust control system, introducing temporal command handling and autonomous execution while preserving architectural clarity and testability.

---

## Scope
Sprint 2 focuses on:
- Command scheduling with explicit durations
- Temporal correctness of command effects
- Automatic background execution of the simulation
- Clear separation between control, execution, and domain logic

Out of scope (for now):
- Fine-grained thread safety
- Real-time guarantees
- Persistence and durability
- Advanced observability and metrics

---

## Implemented features (Sprint 2 — Days 1 to 3)

### Command queue and durations
- Introduction of a command model with remaining execution time
- Command queue managed at the application layer
- Commands persist across multiple simulation steps
- Support for overlapping commands

### Temporal correctness
- Command effects scaled proportionally to the actual time applied within each step
- Correct aggregation of force and torque for partial durations
- Preservation of remaining command time after each step
- Deterministic and testable temporal behavior

### Background simulation execution
- Introduction of a background simulation runner using a dedicated thread
- Automatic periodic execution of simulation steps
- Control over simulation lifecycle: start, pause, resume, stop
- Clear separation between execution infrastructure and application logic

---

## Architecture overview (Sprint 2 additions)

- **Domain**: Remains unchanged and free of execution concerns
- **Application**:
  - Owns command queue and temporal logic
  - Orchestrates simulation execution
  - Exposes lifecycle controls
- **Infrastructure**:
  - Background execution loop
  - Thread-based runner
- **API**:
  - Endpoints for command submission
  - Endpoints for simulation lifecycle control

---

## Key technical decisions
- Use of explicit time integration with proportional time-based scaling of command effects
- Thread-based execution chosen for simplicity and determinism
- Infrastructure introduced only when strictly necessary
- Avoidance of premature locking or concurrency optimizations
- Strong emphasis on correctness and test coverage over performance

---

## Known limitations
- Background runner is not fully thread-safe
- Shared state access is minimally protected
- Simulation timing is approximate (not real-time)
- All state remains in-memory

These limitations are accepted trade-offs at this stage.

---

## Current status
The system now supports:
- Manual and automatic simulation execution
- Time-based command scheduling
- Overlapping control inputs
- Clean lifecycle management

The project is well-positioned for further robustness and infrastructure hardening.

---

## Next steps (Sprint 2 — upcoming)
- Introduce basic thread-safety mechanisms
- Prevent race conditions between API and runner
- Improve execution robustness
- Prepare infrastructure for persistence and observability
