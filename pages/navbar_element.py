from playwright.sync_api import expect
from typing import Literal, Optional,Union

Links = Literal['Documents', 'Users', 'Settings']

Users = Literal['Users','Groups']
Settings = Literal['Preferences', 'Classifications']

class Navbar:
    def __init__(self,page):
        self.page = page
        self.navbarContainer = page.locator('.headerMenu ul.menuList')
        self.navbarLinkDropdown=page.locator('div.headerNavMenu')

    def click_on_link_by_name(self, link:Links, subLink:Optional[Union[Users, Settings]]=None)->None:
        self.navbarContainer.get_by_text(link).click()

        if subLink in Users.__args__:
            self.navbarLinkDropdown.get_by_text(subLink).click()
        elif subLink in Settings.__args__:
            self.navbarLinkDropdown.get_by_text(subLink).click()
        elif subLink is not None:
            print("Invalid subLink argument type.")

