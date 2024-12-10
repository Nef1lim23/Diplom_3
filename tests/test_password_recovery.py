import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.password_recovery_page import PasswordRecoveryPage
from urls import FORGOT_PASS_PAGE


class TestPasswordRecovery:

    @allure.title('переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_click_on_recover_password_button_successful(self, driver, create_user_and_get_creds):
        main_page = MainPage(driver)
        main_page.click_on_login_button()

        login_page = LoginPage(driver)

        current_url = login_page.click_on_button_password_recovery()
        assert current_url == FORGOT_PASS_PAGE

