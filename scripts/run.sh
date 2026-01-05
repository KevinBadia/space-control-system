#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

if [ ! -d ".venv" ]; then
echo "Virtual env not found. Run: ./scripts/setup.sh"
exit 1
fi

# shellcheck disable=SC1091

source .venv/bin/activate

uvicorn app.main:app --reload --host 0.0.0.0 --port 8000