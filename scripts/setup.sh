#!/usr/bin/env bash
set -euo pipefail

# Always run from repo root (even if executed from another folder)

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

PYTHON_BIN="${PYTHON_BIN:-python3}"
VENV_DIR=".venv"

echo "==> Using python: $($PYTHON_BIN --version)"
echo "==> Repo root: $REPO_ROOT"

# Create venv if missing

if [ ! -d "$VENV_DIR" ]; then
echo "==> Creating virtual environment in $VENV_DIR"
$PYTHON_BIN -m venv "$VENV_DIR"
else
echo "==> Virtual environment already exists: $VENV_DIR"
fi

# Activate venv
# shellcheck disable=SC1091

source "$VENV_DIR/bin/activate"

echo "==> Upgrading pip"
python -m pip install --upgrade pip

echo "==> Installing dependencies"
pip install -r requirements.txt

echo "==> Done."
echo ""
echo "Next:"
echo " source .venv/bin/activate"
echo " uvicorn app.main:app --reload --host 0.0.0.0 --port 8000"
echo " python -m pytest"