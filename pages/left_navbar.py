

from typing import Literal


class LeftNavbar:
    def __init__(self,page):
        self.page = page

    def click_on_link(self, link:Literal['Documents']):
        self.page.locator("[data-testid='left-nav']").get_by_text(link).click()
