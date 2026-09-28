import base64
from pathlib import Path

import pytest
import pytest_html
from selenium import webdriver


@pytest.fixture
def driver(request):
    browser = webdriver.Chrome()
    browser.maximize_window()
    request.node.driver = browser

    yield browser

    browser.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call" or not report.failed:
        return

    browser = getattr(item, "driver", None)
    if browser is None:
        return

    screenshot_dir = (
        Path(__file__).resolve().parents[1]
        / "evidence"
        / "screenshots"
    )
    screenshot_dir.mkdir(parents=True, exist_ok=True)

    filename = item.name.replace("[", "_").replace("]", "") + ".png"
    screenshot_path = screenshot_dir / filename
    browser.save_screenshot(str(screenshot_path))

    screenshot_base64 = base64.b64encode(
        screenshot_path.read_bytes()
    ).decode("utf-8")
    report.extras = getattr(report, "extras", []) + [
        pytest_html.extras.image(screenshot_base64, mime_type="image/png")
    ]