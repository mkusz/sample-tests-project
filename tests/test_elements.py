import pytest
from pages import (
    elements_pom,
)


@pytest.mark.somemarker
async def test_go_to_elements_page(
    elements_buttons_page: elements_pom.ElementsButtonsPage
):
    await elements_buttons_page.goto()

    assert await elements_buttons_page.text_element() == "You have done a dynamic click"
