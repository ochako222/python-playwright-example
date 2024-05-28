from pages.login_page import LoginPage
from playwright.sync_api import Page


from global_config.config import base_url
from global_config.config import user

   
def test_valid_login(page: Page)-> None:
    login_page = LoginPage(page)

    page.goto(base_url)
    
    login_page.wait_page_loaded()
    login_page.login_as_user(user)


 