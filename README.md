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
```ecommerce-ui-automation/
├── playwright_ui/             # Python package for the test automation suite
│   ├── bdd_tests/             # Test scripts written in BDD style
│   │   ├── features/          # Gherkin feature files
│   │   ├── step_defs/         # Step definitions for test steps
│   │   ├── pytest_fixtures/   # Custom fixtures for Playwright and other utilities
│   │   └── page_objects/      # Page Object Models for web pages
│   ├── settings/              # Test configuration files
│   ├── utils/                 # Utility functions and helpers
│   └── __init__.py            # Marks this as a Python package
├── tests/                     # Other test scripts (if applicable)
├── .github/                   # GitHub Actions for CI/CD
├── pyproject.toml             # Poetry configuration for dependencies
├── pytest.ini                 # Pytest configuration
├── README.md                  # Project documentation
├── Makefile                   # Automation commands for setup and execution
└── reports/                   # Test execution reports (generated by Allure)
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

### Steps to Run
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/ecommerce-ui-automation.git
   cd ecommerce-ui-automation
   ```
2. **Install dependencies**:
   ```bash
   poetry install
   ```
3. **Run the test suite**:
   ```bash
    pytest -m {marker}
    ```
4. **View the report**:
   ```bash
   allure serve reports/
   ```
---
## Additional Notes

### Key Features
- **Comprehensive Coverage**: Validates authentication, product navigation, checkout, and more.
- **Clean Architecture**: Follows BDD principles, Page Object Models, and modular design.
- **Continuous Integration**: Automates test execution via GitHub Actions.
- **Enhanced Reporting**: Uses Allure for detailed test result visualizations.
- **Pre-commit Hooks**: Ensures code quality with tools like `black` and `isort`.

### Future Improvements
- **Add Edge Case Validations**: For scenarios like invalid user inputs, system timeouts, and performance under load.
- **Expand Cross-Browser Testing**: Include support for multiple browsers (e.g., Firefox, Safari) and mobile platforms.
- **Integrate Visual Testing**: Automate visual regressions to catch UI inconsistencies.