# API Reference — Space Control System

This document describes the REST API exposed by the Space Control System backend.

## Interactive documentation (when running)
When the server is running, interactive documentation is available at:
- `GET /docs` — Swagger UI
- `GET /openapi.json` — OpenAPI schema

---

## Base URL
Local development:
- `http://127.0.0.1:8000`

Codespaces / remote environments:
- Use the forwarded port URL provided by the environment and append the endpoint path (e.g. `/health`, `/docs`).

---

## Endpoints

### 1) Health

#### `GET /health`
Returns a basic health status response.

**Response 200**
```json
{ "status": "ok" }
```

### 2) State
#### `GET /state`
Returns the current spacecraft simulation state.

**Response 200 (example)**
```json
{
  "t": 0.0,
  "x": 0.0,
  "y": 0.0,
  "vx": 0.0,
  "vy": 0.0,
  "theta": 0.0,
  "omega": 0.0
}
```
**Notes**
* Values are floats
* The state is updated only when stepping the simulation.

### 3) History
#### `GET /history?limit=100`
Returns the last `limit` snapshots of the simulation state.

**Query parameters**
* `limit` (int, optional, default = 100): maximum number of snapshots returned

**Response 200 (example)**
```json
[
  {
    "t": 1.0,
    "x": 1.0,
    "y": 0.0,
    "vx": 1.0,
    "vy": 0.0,
    "theta": 0.0,
    "omega": 0.0
  }
]
```
**Notes**
* History is maintained in-memory at the application/service layer.
* History grows only when stepping the simulation.

### 4) Step
#### `POST /step`

Advances the simulation by `dt` seconds and returns the updated state.

**Request body**
```json
{ "dt": 1.0 }
```

**Validation**

* `dt` must be a positive number.
* (If configured) `dt` may be clamped or bounded to avoid numerical instability.

**Response 200 (example)**
```json
{
  "ok": true,
  "state": {
    "t": 1.0,
    "x": 0.0,
    "y": 0.0,
    "vx": 0.0,
    "vy": 0.0,
    "theta": 0.0,
    "omega": 0.0
  }
}
```

**Notes**

* Simulation progression is explicit: time advances only when calling `/step`.
* This design is intentional for determinism and testability.

### 5) Command
#### `POST /command`

Submits a control command that affects the simulation.

**Supported command types**

* apply_force
* apply_torque
* reset

##### `apply_force`

Applies a force vector (intended to affect the next simulation step).

**Request body**
```json
{ "type": "apply_force", "fx": 2.0, "fy": 0.0 }
```

**Response 200**
```json
{ "accepted": true }
```

##### `apply_torque`

Applies a scalar torque (intended to affect the next simulation step).

**Request body**
```json
{ "type": "apply_torque", "torque": 1.0 }
```

**Response 200**
```json
{ "accepted": true }
```

##### `reset`

Resets the simulation state to initial conditions.

**Request body**
```json
{ "type": "reset" }
```

**Response 200**
```json
{ "accepted": true }
```

---

## Simulation Control

These endpoints control the background execution of the simulation.

### POST /run
Starts the background simulation loop.

### POST /pause
Pauses simulation execution without resetting state.

### POST /resume
Resumes simulation execution after a pause.

### POST /stop
Stops the background simulation loop.

---

## Runtime Status

### GET /status
Returns a snapshot of the current runtime state.

Example fields:
- running
- paused
- dt
- queue_length
- history_size
- t

The response represents a read-only snapshot and does not expose internal objects.



---

## Typical usage flow

1. Check server health:

    * `GET /health`

2. Observe the initial state:

    * `GET /state`

3. Submit a command:

    * `POST /command`

4. Advance the simulation:

    * `POST /step`

5. Inspect updated state and history:

    * `GET /state`

    * `GET /history`

---

## Known limitations (Sprint 1)

* Commands affect a single step only (no durations or scheduling yet).
* State and history are stored in-memory.
* The simulation runs only when explicitly stepped via the API.
* Global simulation instance (not designed for concurrency yet).

---