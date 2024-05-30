from playwright.sync_api import expect

from pages.left_navbar import LeftNavbar

class HomePage:
    def __init__(self, page):
        self.page = page
        self.left_navbar = LeftNavbar(page)
    
    def wait_page_loaded(self):
        expect(self.page.locator("[data-testid='header']")).to_be_visible()
        expect(self.page.locator("img[data-testid='header-logo-img']")).to_be_visible()
        expect(self.page.locator("button[data-testid='header-avatar']")).to_be_visible()

    