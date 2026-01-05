# Space Control System — Domain Spec

## 1. System description

This system simulates a simplified 2D spacecraft with translational and rotational dynamics.
The spacecraft evolves in discrete time steps and maintains an internal state defined by position, velocity, orientation and angular velocity.
External control is applied through force and torque commands that affect the system over a limited duration.
The system exposes its current state and recent history via a backend API.
The objective is not high-fidelity physics, but a coherent, testable and extensible control system model.


## 2. State variables
- t: time (s)
- x, y: position
- vx, vy: velocity
- theta: orientation (rad)
- omega: angular velocity (rad/s)

Constants:
- mass (m) > 0
- inertia (I) > 0
- dt > 0

## 3. System dynamics

- Linear acceleration is derived from applied force and mass.
- Angular acceleration is derived from applied torque and inertia.
- State evolution is computed using a discrete-time integration scheme.
- In the absence of control inputs, the system follows inertial motion.


## 4. Commands

### ApplyForce
Applies a constant force to the spacecraft over a specified duration.

Parameters:
- fx: force component along x-axis
- fy: force component along y-axis
- duration: time during which the force is applied

### ApplyTorque
Applies a constant torque to the spacecraft over a specified duration.

Parameters:
- torque: scalar torque value
- duration: time during which the torque is applied

### Reset
Resets the system state to initial conditions.


## 5. Invariants and assumptions

- Simulation time is monotonic: t only increases.
- mass > 0 and inertia > 0.
- dt > 0 and remains constant during execution.
- Orientation angle (theta) is normalized to a fixed range.
- Commands have bounded magnitude and duration.
- If no commands are active, linear and angular velocities remain constant.
- State variables must remain finite (no NaN or infinite values).

## 6. Telemetry and observability

The system exposes:
- Current state snapshot
- Recent state history (last N samples)
- Pending control commands
- System health and simulation status

## 7. Failure modes (non-exhaustive)

- Invalid command parameters
- Numerical instability due to extreme inputs
- State divergence caused by incorrect integration
