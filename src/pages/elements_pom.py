import playwright_helpers
import asyncio


class ElementsButtonsPage(playwright_helpers.PageObjectModelBase):
    @property
    def default_url(self):
        return "https://demoqa.com/buttons"

    async def click_me_button(self):
        await self._page.locator(selector="xpath=//button[text()='Click Me']").click()

    async def text_element(self):
        return await self._page.locator("#dynamicClickMessage").text_content()
