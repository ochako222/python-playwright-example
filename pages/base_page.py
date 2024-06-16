from playwright.sync_api import expect

class BasePage:
    def __init__(self,page):
        self.page = page
    
    def wait_for_array_elements(self,elements:list):
        for el in elements:
            expect(el).to_be_visible()