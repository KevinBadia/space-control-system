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
- [Domain Spec](DOMAIN.md)


## space-control-system repository

### Overview
This project implements a system for simulating and controlling a simplified spacecraft in 2D.

The goal is to design a clean, testable and extensible software architecture that models a physical system and exposes its state and control interface via an API.

The focus is on:
- System modeling
- Backend architecture
- Correct separation of concerns
- Testability and robustness

This is not a UI project, nor a physics-accurate simulator.  
It is an engineering-oriented backend system.

---

## Objectives
- Model a physical system with clear state and dynamics
- Expose system state and telemetry through a REST API
- Accept and validate control commands
- Maintain clean architecture and test coverage
- Serve as a foundation for future data pipelines and analysis

---

## Scope (what this project is / is not)

### In scope
- 2D spacecraft simulation (translation + rotation)
- Discrete-time simulation
- Backend API (FastAPI)
- Domain-driven design
- Unit and integration tests

### Out of scope
- High-fidelity orbital mechanics
- Frontend or visualization
- Real-time guarantees
- Machine learning (for now)

---

## Current status

Sprint 1 completed.

The project currently provides:
- A clean, layered backend architecture
- A deterministic step-based spacecraft simulation
- REST API endpoints for observing and controlling system state
- Test coverage for domain logic and API behavior
- Isolated and reproducible test execution

The system is intentionally simple but structurally sound, serving as a foundation for more advanced control and data features.

---

## Milestones

### Milestone 1 — Core simulation & API ✅
- [x] Domain model defined
- [x] Spacecraft state and dynamics implemented
- [x] Step-based simulation logic
- [x] Health, state, and history endpoints
- [x] Control endpoints (step, commands)
- [x] Test coverage with proper isolation

### Milestone 2 — Robust control & execution loop (planned)
- [ ] Command queue with durations
- [ ] Background simulation loop
- [ ] Improved command validation
- [ ] Pause / resume execution

### Milestone 3 — Data & observability (planned)
- [ ] Telemetry buffering
- [ ] Data export interfaces
- [ ] Performance considerations

---

## Tech stack
- Python 3.11+
- FastAPI
- Pydantic
- Pytest

---

## Design principles

- Clear separation between domain, application, and API layers
- Deterministic and testable simulation logic
- Explicit control over time progression
- Minimal assumptions and controlled scope
- Architecture-first development approach

---

## Status
🚧 Work in progress — active development

