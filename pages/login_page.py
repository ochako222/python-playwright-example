from playwright.sync_api import expect
from global_config.types import User

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.user_name_input = page.locator("#username")
        self.password_input=page.locator("#password")
        self.sign_in_button=page.locator("#submitBtn")

    def wait_page_loaded(self):
        expect(self.user_name_input).to_be_visible()
        expect(self.password_input).to_be_visible()
        expect(self.sign_in_button).to_be_visible()
    
    def login_as_user(self, user:User):
        self.user_name_input.fill(user["user_name"])
        self.password_input.fill(user["password"])
        self.sign_in_button.click()


