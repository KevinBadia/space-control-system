# Sprint 1 — Summary

## Objective
The goal of Sprint 1 was to design and implement a solid backend foundation for a spacecraft control and simulation system.
The focus was on architecture, testability, and clarity rather than physical accuracy or performance.

---

## Scope
Sprint 1 covered:
- Domain modeling of a simplified spacecraft system
- Step-based simulation of translational and rotational dynamics
- Backend API design and implementation
- Test strategy and isolation
- Development environment setup and tooling

Out of scope:
- High-fidelity physics
- Continuous execution loops
- Command scheduling with durations
- Concurrency and scalability concerns

---

## Architecture overview

The system is structured in four main layers:

- **Domain**: Core simulation logic and state representation
- **Application**: Orchestration, state history, and control coordination
- **API**: REST endpoints and request validation
- **Infrastructure**: Execution environment and future integrations

This separation allows incremental evolution without architectural rewrites.

---

## Implemented features

- Spacecraft state representation (position, velocity, orientation)
- Deterministic step-based simulation using explicit integration
- Control commands for force, torque, and reset
- REST endpoints:
  - `/health`
  - `/state`
  - `/history`
  - `/step`
  - `/command`
- Comprehensive test suite covering:
  - Domain behavior
  - API endpoints
  - Error cases
- Test isolation using pytest fixtures

---

## Key technical decisions

- Use of explicit Euler integration for simplicity and predictability
- Singleton simulation service for initial development speed
- Strict separation between domain logic and API concerns
- Emphasis on deterministic behavior and reproducibility
- Avoidance of premature optimization or concurrency

---

## Known limitations

- Simulation advances only via explicit API calls
- Commands affect a single step only
- In-memory state and history
- Global simulation instance (not thread-safe)

These limitations are accepted trade-offs for Sprint 1.

---

## Outcome

Sprint 1 successfully delivered a robust and extensible backend foundation.
The system is well-structured, testable, and ready for more advanced control and execution features.

---

## Next steps (Sprint 2)

- Introduce command durations and command queues
- Implement a background simulation loop
- Improve control realism and robustness
- Prepare telemetry for downstream data pipelines
