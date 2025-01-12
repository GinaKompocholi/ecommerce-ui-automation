import logging
import os
import sys
import time

import allure
import pytest
from playwright.sync_api import sync_playwright

# Files in pytest_plugins will be available to every other file.
# Those files must reside inside a package
pytest_plugins = [
    "ui_automation_suite.bdd_tests.pytest_fixtures.page_fixtures",
    "ui_automation_suite.bdd_tests.step_defs.common_steps",
    "ui_automation_suite.utils.common_fixtures",
]

PLAYWRIGHT_TRACE_DATA_DIR = (
    "ui_automation_suite/bdd_tests/reports/playwright_trace_data"
)


# framework output and logging output are written to the same stream (stdout)
# Add a blank line before logging starts to  place the first log message
# on a new line, making it easier to read.
def pytest_runtest_logstart(nodeid, location):
    print("")


def pytest_configure(config):
    # The `config` parameter is provided by pytest
    # allowing access to command-line options, plugins, and other settings.
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        force=True,
    )  # Reconfigure the logger
    logging.info("Logging configured")


@pytest.fixture()
def browser(request):
    with sync_playwright() as playwright:
        browser = get_browser(request, playwright)
        yield browser
        browser.close()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture()
def page(request, browser):
    context, page = get_page(browser)

    yield page
    test_failed = request.node.rep_call.failed
    if test_failed:
        save_trace(request, context)

    page.close()
    context.close()


def get_browser(request, playwright):
    browser_type = request.config.getoption("--playwright_browser").lower()
    # headless = not request.config.getoption("--headed")

    if browser_type in ["chrome", "firefox"]:
        browser_launcher = getattr(
            playwright, browser_type if browser_type == "firefox" else "chromium"
        )
        browser = browser_launcher.launch(headless=False, slow_mo=666)
    else:
        sys.exit("Provided browser not supported")

    return browser


def get_page(browser):
    context = browser.new_context()
    context.set_default_timeout(timeout=15000)
    context.tracing.start(screenshots=True, snapshots=True)

    page = context.new_page()
    page.set_viewport_size({"width": 1920, "height": 1080})
    return context, page


def save_trace(request, context):
    scenario_name = request.node.originalname
    trace_filename = f"{PLAYWRIGHT_TRACE_DATA_DIR}/trace_{scenario_name}.zip"
    context.tracing.stop(path=trace_filename)

    message = (
        "Step failed: A trace zip file was produced. "
        "Head over to https://trace.playwright.dev/ and drag & drop the file"
    )
    allure.attach(
        message, name="Step failure!", attachment_type=allure.attachment_type.TEXT
    )
    with allure.step(message):
        failed_scenario_name = request.node.name
        # maximum time to wait for the file to be generated after tracing.stop (in
        # seconds)
        max_wait_time = 10
        start_time = time.time()  # remember when we started
        while (
            not os.path.isfile(trace_filename)
            and (time.time() - start_time) < max_wait_time
        ):
            time.sleep(0.3)

        if not os.path.isfile(trace_filename):
            raise FileNotFoundError(
                f"Trace file was not generated within max wait time ({max_wait_time}'')"
            )

        allure.attach.file(
            trace_filename, name=f"trace_{failed_scenario_name}.zip", extension="zip"
        )
    print("Traces saved")


def pytest_addoption(parser):
    """
    Parse cli command to get any other base url in case that we want to run the
    api_tests tests against other test environments such as review apps :param parser:

    :return:
    """
    parser.addoption(
        "--playwright_browser",
        choices=["chrome", "firefox"],
        default="chrome",
        help="Specify the browser to use for Playwright tests",
    )
