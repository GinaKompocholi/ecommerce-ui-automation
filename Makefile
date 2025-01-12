# Variables
MARKER ?= regression  # Default marker is 'regression'

ALLURE_RESULTS_DIR = ui_automation_suite/bdd_tests/reports/allure-results-bdd
ALLURE_REPORT_DIR = ui_automation_suite/bdd_tests/reports/allure-report-bdd
PORT = 8000


# Default target (help menu)
help:
	@echo "Makefile commands:"
	@echo "  make test         Run tests and generate Allure results"
	@echo "  make view-report  Generate and open Allure HTML report"

# Run tests with a marker
test:
	pytest -m $(MARKER)

# Run pre-commit hooks
lint:
	pre-commit run --all-files

# Generate Allure report
generate-report:
	@echo "Generating Allure HTML report..."
	allure generate $(ALLURE_RESULTS_DIR) -o $(ALLURE_REPORT_DIR) --clean

# Generate & view Allure report
generate-view-report: generate-report
	@echo "Click here to view the report: http://localhost:$(PORT)/index.html"
	python3 -m http.server $(PORT) --directory $(ALLURE_REPORT_DIR)
