# Space Control System

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

## Milestones

### Milestone 1 — Core simulation & API
- [ ] Domain model defined
- [ ] Simulation loop implemented
- [ ] State evolution validated
- [ ] Basic API endpoints available

### Milestone 2 — Control & robustness
- [ ] Command validation
- [ ] Error handling
- [ ] Command queue management
- [ ] Improved test coverage

### Milestone 3 — Data & observability
- [ ] State history
- [ ] Telemetry logging
- [ ] Data export interfaces
- [ ] Basic performance considerations

---

## Tech stack
- Python 3.11+
- FastAPI
- Pydantic
- Pytest

---

## Status
🚧 Work in progress — active development

