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
      
    def navigate_to_folder(self,folder_name:str)->None:
        with self.page.expect_response("https://core3.qa.bravais.com/api/v3/folders/root/**") as response:
            self.serachDocumentInput.fill(folder_name)
        assert response.value.ok

        self.page.locator(f'a:has-text("{folder_name}")').click()


