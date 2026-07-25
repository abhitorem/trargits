#!/bin/bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT_DIR"

if command -v python3.11 >/dev/null 2>&1; then
  PYTHON_BIN="$(command -v python3.11)"
elif command -v python3 >/dev/null 2>&1; then
  PYTHON_BIN="$(command -v python3)"
else
  echo "Python 3 was not found. Install it first or set PYTHON_BIN." >&2
  exit 1
fi

echo "Using Python interpreter: $PYTHON_BIN"

if [ ! -d .venv ]; then
  "$PYTHON_BIN" -m venv .venv
fi

source .venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt

echo "Dependencies installed successfully."
echo "Next steps:"
echo "1. In cPanel, create or update the Python app."
echo "2. Set the app root to: $ROOT_DIR"
echo "3. Set the startup file to: passenger_wsgi.py"
echo "4. Restart the app."
