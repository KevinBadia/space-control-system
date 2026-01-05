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


