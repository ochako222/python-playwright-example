from pages import StudioPages
from pages.documents_page import DocumentsPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from playwright.sync_api import Page

from global_config.config import base_url
from global_config.config import user

   
def test_valid_login(page: Page)-> None:
    studio = StudioPages(page)

    page.goto(base_url)
    
    studio.login_page.wait_page_loaded()
    studio.login_page.login_as_user(user)

    studio.home_page.wait_page_loaded()

    studio.home_page.left_navbar.click_on_link('Documents')

    studio.documents_page.wait_page_loaded()




 