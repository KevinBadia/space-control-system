import sqlite3
from pathlib import Path
from typing import Any, Dict, List, Optional

DB_PATH = Path("data") / "telemetry.db"

CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS telemetry (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  t REAL NOT NULL,
  x REAL NOT NULL,
  y REAL NOT NULL,
  vx REAL NOT NULL,
  vy REAL NOT NULL,
  theta REAL NOT NULL,
  omega REAL NOT NULL,
  created_at TEXT NOT NULL DEFAULT (datetime('now'))
);
"""

INSERT_SQL = """
INSERT INTO telemetry (t, x, y, vx, vy, theta, omega)
VALUES (?, ?, ?, ?, ?, ?, ?);
"""

SELECT_LAST_SQL = """
SELECT id, t, x, y, vx, vy, theta, omega, created_at
FROM telemetry
ORDER BY id DESC
LIMIT ?;
"""

SELECT_LATEST_SQL = """
SELECT t, x, y, vx, vy, theta, omega
FROM telemetry
ORDER BY id DESC
LIMIT 1;
"""


class TelemetryRepository:
    def __init__(self, db_path: Path = DB_PATH):
        self.db_path = db_path
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init_db()

    def _connect(self) -> sqlite3.Connection:
        # check_same_thread=False because we may write from runner thread
        conn = sqlite3.connect(self.db_path, check_same_thread=False)
        conn.row_factory = sqlite3.Row
        return conn

    def _init_db(self) -> None:
        with self._connect() as conn:
            conn.execute(CREATE_TABLE_SQL)
            conn.commit()

    def insert_state(self, state: Any) -> None:
        # state is a Pydantic model (State) with attributes we need
        with self._connect() as conn:
            conn.execute(
                INSERT_SQL,
                (state.t, state.x, state.y, state.vx, state.vy, state.theta, state.omega),
            )
            conn.commit()

    def fetch_last(self, limit: int = 100) -> List[Dict[str, Any]]:
        with self._connect() as conn:
            rows = conn.execute(SELECT_LAST_SQL, (limit,)).fetchall()
            return [dict(r) for r in rows]

    def fetch_latest_state(self):
        with self._connect() as conn:
            row = conn.execute(SELECT_LATEST_SQL).fetchone()
            return dict(row) if row else None
