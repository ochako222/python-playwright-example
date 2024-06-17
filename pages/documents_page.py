from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.documents_modal_element import DocumentsModal
from pages.navbar_element import Navbar
from typing import Literal


DropdownOptions = Literal['Archive']

class DocumentsPage(BasePage):
    def __init__(self,page):
        self.page = page
        self.modal = DocumentsModal(page)
        self.navbar = Navbar(page)
        
        self.addDocumentButton = page.locator('[data-cy="add-document-btn"]')
        self.addFolderButton = page.locator('[data-cy="add-folder-btn"]')
        self.serachDocumentInput = page.locator('[data-cy="documents-filter-input"] input')
        self.documentsTable = page.locator('.documents-grid')
        self.add_folder_button = page.locator('.adminContent [data-cy="add-folder-btn"]')
        self.last_breadcramps_element = page.locator('[data-cy="documents-breadcrumbs"] span')
        # self.first_document_in_table = page.locator('.documents-grid [data-id]').first()



    def wait_page_loaded(self):
        self.wait_for_array_elements([self.addDocumentButton, self.addFolderButton,self.serachDocumentInput,self.documentsTable])
      

    def filter_document(self,name:str):
        with self.page.expect_response("https://core3.qa.bravais.com/api/v3/folders/root/**") as response:
            self.serachDocumentInput.fill(name)
        assert response.value.ok

    def navigate_to_folder(self,folder_name:str)->None:
        self.filter_document(folder_name)

        self.page.locator(f'a:has-text("{folder_name}")').click()

    def select_option_for_document_by_name(self,name:str, option:DropdownOptions):
        child=self.page.get_by_text(name)
        parent=self.page.locator('.documents-grid [data-id]').filter(has=child)
        
        parent.locator('[data-field="actions"] >div>div').click()

        if option=='Archive':
            option_locator = '[data-cy="archive-menu-item"]'
        
        self.page.locator(option_locator).click()
        

    def click_on_add_folder(self)->None:
        self.add_folder_button.click()

    def get_docuument_by_name(self, name:str):
       return self.page.locator(f'.documents-grid [data-id] a:has-text("{name}")')



    


