import asyncio
import time
from typing import Optional

import playwright.async_api as playwright
import pydantic


class PlaywrightConfig(pydantic.BaseSettings):
    """Playwright settings model"""

    class Config:
        env_prefix = "QA_PLAYWRIGHT_"
        allow_mutation = False

    browser: str = "chrome"
    headless: bool = True
    proxy_server: Optional[str] = None
    proxy_user: Optional[str] = None
    proxy_pass: Optional[str] = None
    proxy_bypass: Optional[str] = None

    @property
    def proxy(self) -> Optional[playwright.ProxySettings]:
        if self.proxy_server:
            settings: playwright.ProxySettings = {"server": self.proxy_server}
            return settings
        return None


class PageObjectModelBase:
    def __init__(self, page: playwright.Page):
        self._page: playwright.Page = page

    @property
    def default_url(self):
        """Returns default url of the given web page."""
        raise NotImplementedError

    @property
    def current_url(self):
        """Return current browser url"""
        return self._page.url

    async def wait_for_url(
        self,
        timeout: int = 120,  # 2 min
        url_beginning: Optional[str] = None,
    ):
        timeout_start = time.perf_counter()
        timeout_end = time.perf_counter() + timeout
        while time.perf_counter() <= timeout_end:
            await asyncio.sleep(0.5)
            if (not url_beginning and self.current_url == self.default_url) or (
                url_beginning and self.current_url.startswith(url_beginning)
            ):
                break
        else:
            raise TimeoutError(
                f"Current url: '{self.current_url}' does not match expected: "
                f"'{url_beginning if url_beginning else self.default_url}'"
            )

    async def goto(self):
        await self._page.goto(self.default_url)
