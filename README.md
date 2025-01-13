# ecommerce-ui-automation

## Overview
This repository contains a **UI automation suite** developed to validate the functionality of the e-commerce website [SauceDemo](https://www.saucedemo.com/). The project demonstrates modern test automation practices, including Behavior-Driven Development (BDD), Page Object Model (POM), and CI/CD pipelines.

The goal of this project is to showcase:
- Test automation capabilities.
- Framework setup, structure, and scalability.
- Integration with tools like reporting, CI/CD pipelines, and pre-commit hooks.

---

## Features Tested
This automation suite validates critical functionalities of the [SauceDemo](https://www.saucedemo.com/) website:
1. **Authentication**: Login and logout functionality.
2. **Products Page**: Verifying product listings and navigation.
3. **Add to Cart**: Adding items to the shopping cart.
4. **Checkout**: Completing the checkout process.
5. **Burger Menu**: Validating navigation options.

Each test is designed to ensure coverage of happy paths, edge cases, and negative scenarios.

---

## Project Structure
The project is organized with a clear folder structure to ensure scalability and maintainability:
```
ecommerce-ui-automation/
├── .github/                   # GitHub Actions for CI/CD
│   └── workflows/
│       └── run_ui_tests.yml   # Workflow configuration for CI pipeline
├── .pytest_cache/             # Pytest's cache directory (auto-generated, git-ignored)
├── ui_automation_suite/       # Python package for the test automation suite
│   ├── bdd_tests/             # Test scripts written in BDD style
│   │   ├── features/          # Gherkin feature files
│   │   ├── step_defs/         # Step definitions for test steps
│   │   ├── pytest_fixtures/   # Custom fixtures for Playwright and other utilities
│   │   └── page_objects/      # Page Object Models for web pages
│   ├── settings/              # Test configuration files
│   ├── utils/                 # Utility functions and helpers
│   └── __init__.py            # Marks this as a Python package
├── reports/                   # Test execution reports (generated by Allure and Playwright traces)
│   ├── allure-report-bdd/     # Generated Allure HTML reports
│   ├── allure-results-bdd/    # Raw results for Allure
│   └── playwright_trace_data/ # Trace data generated by Playwright
├── .env                       # Environment variables (git-ignored)
├── .gitignore                 # Excludes unnecessary files from version control
├── .pre-commit-config.yaml    # Pre-commit hooks for code quality checks
├── conftest.py                # Pytest's configuration and shared fixtures
├── Makefile                   # Automation commands for setup and execution
├── pyproject.toml             # Poetry configuration for dependencies
├── pytest.ini                 # Pytest configuration
├── README.md                  # Project documentation
└── poetry.lock                # Poetry's lock file for dependencies
```
---

## Technology Stack
The suite is built using the following technologies:
- **Test Automation Framework**: [Playwright](https://playwright.dev/)
- **BDD Framework**: [pytest-bdd](https://pytest-bdd.readthedocs.io/)
- **Reporting**: [Allure](https://docs.qameta.io/allure/)
- **Dependency Management**: [Poetry](https://python-poetry.org/)
- **CI/CD**: GitHub Actions
- **Code Quality**: pre-commit hooks (`black`, `isort`) for linting and formatting
- **Logging**: Python logging for debugging insights

---

## Setup and Execution
### Prerequisites
- Python 3.11 or later installed.
- Poetry installed (for dependency management).

### Steps to Run tests locally
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/ecommerce-ui-automation.git
   cd ecommerce-ui-automation
   ```
2. **Install dependencies**:
   ```bash
   poetry install
   ```
3. **Run the complete test suite**:
   ```bash
    make test
    ```
4. **View the report**:
   ```bash
   make view-report
   ```
   Then click on the link to view the report in the browser
---
### Hosted Allure Report


For executions triggered by [GitHub Actions](https://github.com/GinaKompocholi/ecommerce-ui-automation/actions/workflows/run_ui_tests.yml), Allure report is automatically generated and hosted online.
You can view the latest CI-generated report [here](https://ginakompocholi.github.io/ecommerce-ui-automation/)
---
### Ways to Run Tests

The test suite offers various execution modes for flexibility.

1. **Run the complete test regression suite**
   1. Headless Mode
      ```bash
      make test
      ```
   2. Headed Mode
      ```bash
      make test-headed
      ```
2. **Run a specific test**:
   1. Headless Mode
      ```bash
      make test "MARKER=login_success"
      ```
   2. Headed Mode
      ```bash
      make test-headed "MARKER=login_success"
      ```

3. **Change Browser (default: chromium)**
   1. Headless Mode
      ```bash
      make test "BROWSER=firefox"
      ```
   2. Headed Mode
      ```bash
      make test-headed "BROWSER=firefox"
      ```
4. **Debug Mode (Runs only in headed mode)**
   1. Run step-by-step:
      ```bash
      make test-debug
      ```
   2. Combine with specific marker and browser:
      ```bash
      make test-debug "MARKER=login_success" "BROWSER=firefox"
      ```

## Additional Notes

### Key Features
- **Comprehensive Coverage**: Validates authentication, product navigation, checkout, and more.
- **Clean Architecture**: Follows BDD principles, Page Object Models, and modular design.
- **Continuous Integration**: Automates test execution via GitHub Actions.
- **Enhanced Reporting**: Uses Allure for detailed test result visualizations.
- **Pre-commit Hooks**: Ensures code quality with tools like `black` and `isort`.

### Future Improvements
- **Integrate Visual Testing**: Automate visual regression testing to detect UI inconsistencies and layout shifts effectively.
- **Extend Test Coverage**: Add more test scenarios for edge cases and negative paths.
- **Parallelize Test Execution Across Browsers**: Optimize test runtime by running tests simultaneously in multiple browsers (e.g., Chrome, Firefox, Safari). 
- **Automate Local Report Management**: Implement a local mechanism to keep only the latest test report for easy access while automatically deleting older reports to reduce clutter.
- **Centralize Report Storage for Historical Analysis**:  Implement a system to upload and store test results in a centralized location (e.g., S3 bucket, database, or CI tool dashboard) to maintain a history of test executions, allowing trend analysis and debugging over time.
- **Cross-Device Testing**: Extend test suite to simulate and verify functionality across different device types (e.g. mobile, tablet)