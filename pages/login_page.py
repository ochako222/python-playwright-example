from playwright.sync_api import expect
from global_config.types import User


class LoginPage:
    def __init__(self, page):
        self.page = page
        self.user_name_input = page.locator("[name='username']")
        self.search_button = page.locator('#search_button_homepage')
        self.password_input=page.locator("[name='password']")
        self.continue_button=page.locator("[data-testid='username-check-button']")
        self.sign_in_button=page.locator("[data-testid='login-submit-button']")

    
    def wait_page_loaded(self):
        expect(self.user_name_input).to_be_visible()
        expect(self.continue_button).to_be_visible()

    
    def login_as_user(self, user:User):
        self.page.wait_for_timeout(3500)
        self.user_name_input.fill(user["user_name"])
        self.continue_button.click()

        self.password_input.fill(user["password"])
        self.sign_in_button.click()


