import pytest
from pages import PortalPages
from playwright.sync_api import Page
from playwright.sync_api import expect

from global_config.config import user, base_url

@pytest.fixture(autouse=True)
def before_hook(page: Page):
    portal = PortalPages(page)

    page.goto(base_url)
    
    portal.login_page.wait_page_loaded()
    portal.login_page.login_as_user(user)


def test_create_remove_document(page: Page)-> None:
    portal = PortalPages(page)
    portal.home_page.wait_page_loaded()

    portal.home_page.navbar.click_on_link_by_name('Documents')
    portal.documents_page.wait_page_loaded()


    portal.documents_page.click_on_add_folder()

    new_folder = 'PYTHON_FOLDER'

    portal.documents_page.modal.fill_in_new_folder_form(new_folder, 'description')
    expect(portal.documents_page.last_breadcramps_element).to_have_text(new_folder)

    portal.documents_page.navbar.click_on_link_by_name('Documents')
    portal.documents_page.wait_page_loaded()

    portal.documents_page.filter_document(new_folder)
    expect(portal.documents_page.get_docuument_by_name(new_folder)).to_be_visible()

    portal.documents_page.select_option_for_document_by_name(new_folder,'Archive')
    portal.documents_page.modal.confirm_archieving()

    expect(portal.documents_page.get_docuument_by_name(new_folder)).not_to_be_visible()
    
  


