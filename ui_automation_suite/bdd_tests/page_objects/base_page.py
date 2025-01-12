from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def refresh_page(self):
        self.page.reload()

    def get_current_url(self) -> str:
        return self.page.url

    def get_element_text(self, selector: str) -> str:
        return self.page.locator(selector).text_content()

    def wait_until_page_has_loaded(self):
        self.page.wait_for_selector("html", state="visible")
