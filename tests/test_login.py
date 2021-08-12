from pages.login_page import LoginPage

class TestLoginPage():

    def test_login_valid(self, browser):
        login_page = LoginPage(browser)
        login_page.load()
        login_page.set_email_field("misteraladinqa@gmail.com")
        login_page.click_next_button()
        login_page.set_password_field("@MisterA1")
        login_page.click_sign_in_button()
        