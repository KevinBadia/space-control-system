# Sprint 3 — Summary

## Objective
The goal of Sprint 3 is to add persistence and observability to the system, allowing it to retain state across restarts, expose meaningful runtime metrics, and provide operational visibility through logs and status endpoints.

---

## Scope
Sprint 3 focuses on:
- Persisting simulation state and telemetry using SQLite
- Rehydrating the system state on startup
- Exporting telemetry for external analysis
- Structured logging with runtime context
- Runtime observability via status and metrics endpoints

Out of scope:
- Distributed persistence
- Real-time guarantees
- Advanced monitoring stacks (Prometheus, Grafana, etc.)
- Long-term data retention policies

---

## Implemented features

### SQLite persistence
- Automatic creation of a local SQLite database (`data/telemetry.db`)
- Telemetry table storing state snapshots per simulation step
- Thread-safe access to SQLite from background execution
- Each simulation step persists one telemetry record

### State rehydration
- On startup, the system loads the latest persisted state (if available)
- Clean initial state is used when persistence is disabled or no data exists
- Configurable behavior to disable DB loading for deterministic testing

### Telemetry access and export
- Endpoint to retrieve recent telemetry rows
- CSV and JSON export via HTTP response
- Export is generated in-memory (no server-side file creation)
- Client-controlled storage of exported data

### Observability and logging
- Structured logging using Python standard logging
- Periodic runtime logs during simulation execution
- Logs include step count, simulation time, queue size, and history size
- Centralized logging configuration at application startup

### Runtime status and metrics
- `/status` endpoint exposes a snapshot of runtime state:
  - runner status (running/paused)
  - uptime
  - step count
  - simulation time
  - queue length
  - history size
- Snapshot-based access ensures thread-safe, read-only inspection

---

## Architecture overview (Sprint 3 additions)

- **Infrastructure**
  - SQLite-based telemetry repository
  - Logging configuration module

- **Application**
  - Optional state rehydration during initialization
  - Runtime metrics tracking
  - Snapshot-based status reporting

- **API**
  - Telemetry retrieval and export endpoints
  - Extended status endpoint for observability

---

## Key technical decisions
- SQLite chosen for simplicity, portability, and robustness
- Persistence handled at the application layer, not domain
- Snapshot-based reads to avoid exposing mutable internal state
- Logging via standard library to avoid unnecessary dependencies
- Persistence optional and configurable to preserve test determinism

---

## Known limitations
- Persistence is local and single-process only
- Logging is console-based
- Telemetry storage grows unbounded
- Metrics are approximate and not real-time accurate

These are acceptable trade-offs for the current stage.

---

## Current status
The system now:
- Persists and reloads state across restarts
- Exposes telemetry for inspection and export
- Provides runtime observability through logs and status
- Remains testable and deterministic

Sprint 3 significantly improves system operability and debuggability.

---

## Next steps
Sprint 4 will focus on:
- Control extensibility
- Scheduling and scenarios
- Further robustness and cleanup
- Preparing the system for more complex use cases
