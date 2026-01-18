# Space Control System

![Python](https://img.shields.io/badge/python-3.11%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![Tests](https://img.shields.io/badge/tests-pytest-informational)

[![Last Commit](https://img.shields.io/github/last-commit/KevinBadia/space-control-system)](https://github.com/KevinBadia/space-control-system/commits/main)
![Commit Activity](https://img.shields.io/github/commit-activity/m/KevinBadia/space-control-system)
![Repo Size](https://img.shields.io/github/repo-size/KevinBadia/space-control-system)
![License](https://img.shields.io/github/license/KevinBadia/space-control-system)
![Issues](https://img.shields.io/github/issues/KevinBadia/space-control-system)

## Quick links
- [API Docs](http://127.0.0.1:8000/docs)
- [Sprint 1 Summary](SPRINT_1_SUMMARY.md)
- [Sprint 2 Summary](SPRINT_2_SUMMARY.md)
- [Sprint 3 Summary](SPRINT_3_SUMMARY.md)
- [Domain Spec](DOMAIN.md)
- Simulation control: `/run`, `/pause`, `/resume`, `/stop`

---

## API
See [API.md](API.md) for endpoint documentation.

---

## Overview
This project implements a backend system for simulating and controlling a simplified spacecraft in 2D.

The goal is to design a **clean, testable, and extensible software architecture** that models a physical system and exposes its state, telemetry, and control interfaces via a REST API.

The focus is on:
- System modeling
- Backend architecture
- Correct separation of concerns
- Determinism and testability
- Observability and robustness

This is **not** a UI project, nor a physics-accurate simulator.  
It is an **engineering-oriented backend system**.

---

## Objectives
- Model a physical system with clear state and dynamics
- Expose system state and telemetry through a REST API
- Accept, schedule, and validate control commands
- Persist and reload state across restarts
- Provide runtime observability and diagnostics
- Maintain clean architecture and strong test coverage

---

## Scope (what this project is / is not)

### In scope
- 2D spacecraft simulation (translation + rotation)
- Discrete-time simulation
- Background execution loop
- Backend API (FastAPI)
- Domain-driven design
- SQLite-based telemetry persistence
- Structured logging and runtime metrics
- Unit and integration tests

### Out of scope
- High-fidelity orbital mechanics
- Frontend or visualization
- Real-time guarantees
- Distributed systems
- Machine learning (for now)

---

## Current Status

The system currently supports:
- Time-based command scheduling with explicit durations
- Correct temporal scaling of command effects
- Automatic background simulation execution
- Lifecycle control via API (run, pause, resume, stop)
- Minimal thread-safety through application-level locking
- Snapshot-based runtime state inspection
- SQLite-based telemetry persistence
- State rehydration on application startup
- Telemetry export via CSV or JSON
- Structured runtime logging

The system is intentionally simple but structurally sound, serving as a solid foundation for more advanced control, data, and analysis features.

---

## Milestones

### Milestone 1 — Core simulation & API ✅
- [x] Domain model defined
- [x] Spacecraft state and dynamics implemented
- [x] Step-based simulation logic
- [x] Health, state, and history endpoints
- [x] Control endpoints (step, commands)
- [x] Test coverage with proper isolation

### Milestone 2 — Robust control & execution loop ✅
- [x] Command queue with durations
- [x] Temporal correctness for partial command execution
- [x] Background simulation loop
- [x] Pause / resume execution
- [x] Thread-safety for concurrent access

### Milestone 3 — Persistence & observability 🚧
- [x] SQLite-based telemetry persistence
- [x] State reload on startup
- [x] Telemetry export interfaces (CSV / JSON)
- [x] Structured logging
- [x] Runtime status and metrics
- [ ] Long-term retention strategy
- [ ] Advanced observability (optional)

---

## Tech stack
- Python 3.11+
- FastAPI
- Pydantic
- SQLite
- Pytest

---

## Design principles
- Clear separation between domain, application, infrastructure, and API layers
- Deterministic and testable simulation logic
- Explicit control over time progression
- Snapshot-based state exposure
- Infrastructure introduced only when necessary
- Architecture-first development approach

---

## Status
🚧 Work in progress — active development
