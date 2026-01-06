# Worklog - Space Control System

## Day 1–5 — Project setup, architecture, and core backend implementation
**Date:** 2026-01-05  
**Time spent:** ~3 hours  

### What I did
- Created the repository and defined a clean initial project structure.
- Defined the system domain and scope in DOMAIN.md, focusing on a simplified spacecraft control and simulation backend.
- Set up a layered architecture separating domain, application, API, and infrastructure concerns.
- Implemented a FastAPI backend skeleton with health checks and OpenAPI documentation.
- Modeled spacecraft state and dynamics, including translational and rotational motion.
- Implemented a step-based simulation using explicit time integration.
- Exposed REST endpoints to observe and control the system state (`/health`, `/state`, `/history`, `/step`, `/command`).
- Added support for control commands (force, torque, reset) through validated API requests.
- Implemented state history tracking at the application layer.
- Wrote unit and integration tests for both domain logic and API behavior.
- Ensured test isolation by resetting shared simulation state between tests using pytest fixtures.

### Key technical decisions
- Chose explicit Euler integration for simplicity, determinism, and testability.
- Used a singleton simulation service for the initial sprint to reduce complexity.
- Kept domain logic free of API and infrastructure concerns.
- Centralized orchestration logic in an application service layer.
- Prioritized testability and deterministic behavior over realism or performance.

### Problems encountered
- Test failures due to shared mutable state across tests.
- Import resolution issues caused by missing Python package initialization.
- Initial confusion around API exposure in a Codespaces environment.

### How they were solved
- Introduced a pytest fixture to reset the simulation state before each test.
- Added `__init__.py` files to ensure proper Python package discovery.
- Adjusted server startup configuration and endpoint access for the development environment.

### Lessons learned
- Test isolation is critical when working with shared state.
- Clean architecture significantly simplifies incremental development.
- Separating domain logic from API concerns makes systems easier to reason about and test.
- FastAPI’s TestClient enables fast, reliable testing without running a live server.

### Next steps
- Improve command handling with durations and command queues.
- Introduce a background simulation loop.
- Add data export and observability features.
- Refine architecture for concurrency and scalability.


## Day 6: Background execution and infrastructure
**Date:** 2026-01-06  
**Time spent:** ~2–3 hours  

### What I did
- Implemented a background simulation runner using a dedicated thread.
- Introduced automatic periodic execution of simulation steps.
- Added lifecycle controls to the application layer (run, pause, resume, stop).
- Exposed simulation lifecycle control endpoints through the API.
- Added basic tests to validate automatic time progression.
- Ensured infrastructure responsibilities remained isolated from domain logic.

### Key decisions
- Chose a thread-based execution model over asyncio for simplicity and clarity.
- Introduced infrastructure only after control logic was stable.
- Kept execution control centralized in the application layer.
- Accepted limited thread-safety as a conscious short-term trade-off.

### Problems encountered
- Coordinating background execution without polluting domain logic.
- Ensuring the runner could be cleanly started and stopped.

### How they were solved
- Introduced a dedicated infrastructure component for execution.
- Used clear lifecycle states and explicit control methods.
- Validated behavior through targeted integration tests.

### Lessons learned
- Introducing infrastructure later significantly simplifies design.
- Explicit lifecycle control improves system observability and debuggability.
- Separating execution from control is critical for system evolution.

### Next steps
- Add basic thread-safety mechanisms.
- Harden infrastructure for concurrent access.
- Continue Sprint 2 with robustness improvements.
