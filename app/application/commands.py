from dataclasses import dataclass
from typing import Optional


@dataclass
class Command:
    type: str
    fx: float = 0.0
    fy: float = 0.0
    torque: float = 0.0
    remaining_time: float = 0.0