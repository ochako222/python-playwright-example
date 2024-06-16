from playwright.sync_api import expect
from pages.base_page import BasePage


class DocumentsPage(BasePage):
    def __init__(self,page):
        self.page = page
        self.addDocumentButton = page.locator('[data-cy="add-document-btn"]')
        self.addFolderButton = page.locator('[data-cy="add-folder-btn"]')
        self.serachDocumentInput = page.locator('[data-cy="documents-filter-input"] input')
        self.documentsTable = page.locator('.documents-grid')

    def wait_page_loaded(self):
        self.wait_for_array_elements([self.addDocumentButton, self.addFolderButton,self.serachDocumentInput,self.documentsTable])
      