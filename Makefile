.PHONY: setup run test clean help

setup:
	./scripts/setup.sh

run:
	./scripts/run.sh

test:
	./scripts/test.sh

clean:
	rm -rf .venv __pycache__ .pytest_cache

help:
	@echo "Available commands:"
	@echo "  make setup  - Create venv and install dependencies"
	@echo "  make run    - Run API server"
	@echo "  make test   - Run tests"
	@echo "  make clean  - Remove venv and caches"
