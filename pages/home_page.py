from playwright.sync_api import expect
from pages.navbar_element import Navbar


class HomePage:
    def __init__(self, page):
        self.page = page
        self.navbar = Navbar(page)
        self.favoritesContainer = page.locator(".home-favorites")
        self.latestUpdates = page.locator('[data-cy="home-latest-section"]')
        self.recentDocuments = page.locator('[data-cy="home-recent-section"]')
    
    def wait_page_loaded(self):
        expect(self.favoritesContainer).to_be_visible()
        expect(self.latestUpdates).to_be_visible()
        expect(self.recentDocuments).to_be_visible()

    