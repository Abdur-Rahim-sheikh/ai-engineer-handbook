import pytest

from playwright.sync_api import Page, expect  # noqa: F401


@pytest.mark.ui
@pytest.mark.acme_bank
def test_acme_bank_login(page: Page):
    page.goto("https://demo.applitools.com/")
    page.fill("#username", "test_user")
    page.fill("#password", "test_pass")
    page.click("#log-in")
    # expect(page.locator("#time")).to_be_visible()
    # time_text = page.locator("#time").inner_text()
    # assert re.match(r"\d{2}:\d{2}:\d{2}", time_text), "Time format is incorrect"

    expect(page.locator("div.logo-w")).to_be_visible()
    expect(page.locator("ul.main-menu")).to_be_visible()
    expect(page.get_by_text("Add Account")).to_be_visible()
    expect(page.get_by_text("Make Payment")).to_be_visible()
    expect(page.get_by_text("View Statement")).to_be_visible()
    expect(page.get_by_text("Request Increase")).to_be_visible()
    expect(page.get_by_text("Pay Now")).to_be_visible()
