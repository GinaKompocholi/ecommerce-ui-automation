MARKER ?= regression  # Default marker is 'regression'
BROWSER ?= chrome  # Default browser is 'chromium'

ALLURE_RESULTS_DIR = ui_automation_suite/bdd_tests/reports/allure-results-bdd
ALLURE_REPORT_DIR = ui_automation_suite/bdd_tests/reports/allure-report-bdd
PORT = 8000


# Default target (help menu)
help:
	@echo "Makefile commands:"
	@echo "  make test         Run tests and generate Allure results"
	@echo "  make generate-and-view-report  Generate and open Allure HTML report"

# Run tests with a marker in headless mode
test:
	pytest -m $(MARKER) --playwright_browser=$(BROWSER)

# Run tests with a marker in headed mode
test-headed:
	pytest -m $(MARKER) --headed --playwright_browser=$(BROWSER)

# Run tests in debug mode (headed mode by default)
test-debug:
	PWDEBUG=1 pytest -m $(MARKER) --playwright_browser=$(BROWSER)

# Run pre-commit hooks
lint:
	pre-commit run --all-files

# Generate Allure report
generate-report:
	@echo "Generating Allure HTML report..."
	allure generate $(ALLURE_RESULTS_DIR) -o $(ALLURE_REPORT_DIR) --clean

# Generate & view Allure report
generate-and-view-report: generate-report
	@echo "Click here to view the report: http://localhost:$(PORT)/index.html"
	python3 -m http.server $(PORT) --directory $(ALLURE_REPORT_DIR)
