from pages.documents_page import DocumentsPage
from pages.home_page import HomePage
from pages.login_page import LoginPage


class StudioPages:
    def __init__(self, page):
        self.documents_page = DocumentsPage(page)
        self.login_page = LoginPage(page)
        self.home_page = HomePage(page)
   
