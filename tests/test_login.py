from pages import PortalPages
from playwright.sync_api import Page
from playwright.sync_api import expect

from global_config.config import user, base_url

def test_valid_login(page: Page)-> None:
    portal = PortalPages(page)

    page.goto(base_url)
    
    portal.login_page.wait_page_loaded()
    portal.login_page.login_as_user(user)

    portal.home_page.wait_page_loaded()

    portal.home_page.navbar.click_on_link_by_name('Documents')

    portal.documents_page.wait_page_loaded()
    portal.documents_page.navigate_to_folder('AUTOMATION_TESTS_FOLDER')


def test_invalid_login(page:Page)-> None:
    portal = PortalPages(page)

    page.goto(base_url)

    portal.login_page.wait_page_loaded()
    portal.login_page.login_as_user({'user_name':'wrong_user@gmail.com','password':'wrong_password'})

    expect(portal.login_page.alert_message).to_have_text('The username or password is incorrect.')


 