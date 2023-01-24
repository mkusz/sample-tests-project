import playwright.async_api as playwright
import pytest_asyncio
import playwright_helpers
from pages import (
    elements_pom,
)

@pytest_asyncio.fixture
async def page() -> playwright.Page:  # type: ignore
    async with playwright.async_playwright() as playwright_obj:
        browser_settings = playwright_helpers.PlaywrightConfig()

        browser = await playwright_obj.chromium.launch(
            channel=browser_settings.browser,
            headless=bool(browser_settings.headless),
            proxy=browser_settings.proxy,
            args=["--disable-gpu"],
        )
        try:
            new_page: playwright.Page = await browser.new_page(record_video_dir="reports/")
            async with new_page as page:
                await  page.set_viewport_size({"width": 1280, "height": 1024})
                page.set_default_navigation_timeout(120000)  # 2 min
                page.set_default_timeout(60000)  # 1 min
                yield page
        finally:
            await browser.close()


@pytest_asyncio.fixture
async def elements_buttons_page(
    page: playwright.Page,
) ->elements_pom.ElementsButtonsPage:
    return elements_pom.ElementsButtonsPage(page=page)
