from pages.login_page import LoginPage
from playwright.sync_api import Page

from objects.types import User

user:User={
    "user_name":'oleksandr.chako@xyleme.com',
    "password":'Mypass@123'
}

   
def test_valid_login(page: Page)-> None:
    login_page = LoginPage(page)

    page.goto('https://studio-elevate.qa.xyleme.com')

    login_page.wait_page_loaded()
    login_page.login_as_user(user)


 