from playwright.sync_api import Page
from playwright.sync_api import expect
from objects.types import User


class LoginPage:
    def __init__(self, page):
        self.page = page
        self.user_name_input = page.locator("[name='username']")
    
    @property
    def password_input(self):
        return self.page.locator("[name='password']")
    
        
    @property
    def continue_button(self):
        return self.page.locator("[data-testid='username-check-button']")
    
    @property
    def sign_in_button(self):
        return self.page.locator("[data-testid='login-submit-button']")
    
    def wait_page_loaded(self):
        expect(self.user_name_input).to_be_visible()
        expect(self.continue_button).to_be_visible()

    
    def login_as_user(self, user:User):
        self.page.wait_for_timeout(3500)
        self.user_name_input.fill(user["user_name"])
        self.continue_button.click()

        self.password_input.fill(user["password"])
        self.sign_in_button.click()


