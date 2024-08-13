from playwright.sync_api import expect
from typing import Literal, Optional,Union

class DocumentsModal:
    def __init__(self,page):
        self.page = page
        # New folder modal
        self.new_folder_name_input = page.locator('[data-cy="name-text-field"] input')
        self.new_folder_description_input = page.locator('[data-cy="description-text-area"]')
        self.confirm_new_folder_button = page.locator('[data-cy="save-button"]')
        # Archive modal
        self.confirm_archieve_button = page.locator('[data-cy="archive-button"]')

    def fill_in_new_folder_form(self, name:str, description:str)->None:
        self.new_folder_name_input.fill(name)
   
        self.new_folder_description_input.fill(description)
        self.confirm_new_folder_button.click()

    def confirm_archieving(self):
        with self.page.expect_response("") as response:
            self.confirm_archieve_button.click()
        assert response.value.ok