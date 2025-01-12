# Variables
MARKER ?= regression  # Default marker is 'regression'

# Default target
help:
	@echo "Makefile commands:"
	@echo "  make test [MARKER=<marker>]    Run pytest tests with a specific marker (default: regression)"
	@echo "  make lint                     Run pre-commit checks on all files"

# Run tests with a marker
test:
	pytest -m $(MARKER)

# Run pre-commit hooks
lint:
	pre-commit run --all-files
