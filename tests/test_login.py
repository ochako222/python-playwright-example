from pages import PortalPages
from playwright.sync_api import Page

from global_config.config import user, base_url

   
def test_valid_login(page: Page)-> None:
    portal = PortalPages(page)

    page.goto(base_url)
    
    portal.login_page.wait_page_loaded()
    portal.login_page.login_as_user(user)

    portal.home_page.wait_page_loaded()

    portal.home_page.navbar.click_on_link_by_name('Documents')

    portal.documents_page.wait_page_loaded()

    page.pause()




 