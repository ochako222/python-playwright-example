from playwright.sync_api import expect

class DocumentsPage:
    def __init__(self,page):
        self.page = page

    def wait_page_loaded(self):
        expect(self.page.locator(".layout-container .search-container")).to_be_visible()
        expect(self.page.locator(".layout-container button:has-text('New document')")).to_be_visible()
        expect(self.page.locator(".layout-container button:has-text('New folder')")).to_be_visible()
        expect(self.page.locator(".layout-container .documents-body-table-container")).to_be_visible()