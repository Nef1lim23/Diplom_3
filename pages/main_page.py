import allure
from pages.base_page import BasePage
from pages_locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.title('Клик на кнопку Войти в аккаунт')
    def click_on_login_button(self):
        login_button = self.find_element_with_wait(MainPageLocators.LOGIN_BUTTON)
        self.click_on_element_js(login_button)

    def wait_page_to_be_loaded(self):
        self.find_element_with_wait(MainPageLocators.BUTTON_CREATE_ORDER)

    @allure.step("Клик на кнопку -> Личный кабинет")
    def click_on_personal_account_button(self, url):
        personal_account_button = self.find_element_with_wait(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        self.click_on_element_js(personal_account_button)
        self.wait_url_to_be(url)
        return self.current_url()
