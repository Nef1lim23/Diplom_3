import allure

from pages.base_page import BasePage
from pages_locators.personal_account_locators import PersonalAccountPageLocators
from urls import ORDER_HISTORY_PAGE


class PersonalAccountPage(BasePage):

    @allure.title('Клик на кнопку "История заказов"')
    def click_on_order_history(self):
        order_history = self.find_element_with_wait(PersonalAccountPageLocators.ORDER_HISTORY)
        self.click_on_element_js(order_history)
        self.wait_url_to_be(ORDER_HISTORY_PAGE)
        return self.current_url()

    @allure.title('Клик на выход из аккаунта')
    def click_on_log_out_from_acc(self, url):
        log_out = self.find_element_with_wait(PersonalAccountPageLocators.BUTTON_LOG_OUT)
        self.click_on_element_js(log_out)
        self.wait_url_to_be(url)
        return self.current_url()

    @allure.title('Получение номера заказа из истории заказов')
    def get_number_order_from_history_order(self):
        get_number_order = self.get_text_from_element(PersonalAccountPageLocators.ORDER)
        return get_number_order
