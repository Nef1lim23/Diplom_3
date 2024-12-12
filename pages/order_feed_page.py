import allure

from pages.base_page import BasePage
from pages_locators.order_feed_locators import OrderFeedLocators
from urls import MAIN_PAGE


class OrderFeedPage(BasePage):

    @allure.title('Клик на кнопку "Конструктор"')
    def click_on_button_constructor(self):
        button_constructor = self.find_element_with_wait(OrderFeedLocators.BUTTON_CONSTRUCTOR)
        self.click_on_element_js(button_constructor)
        self.wait_url_to_be(MAIN_PAGE)
        return self.current_url()

    @allure.title('Клик на заказ')
    def click_on_order(self):
        order = self.find_element_with_wait(OrderFeedLocators.ORDER)
        self.click_on_element_js(order)

    @allure.title('Проверка видимости окна создания заказа')
    def order_window_is_visible(self):
        title_modal_window = self.find_element_with_wait(OrderFeedLocators.ORDER_MODAL_WINDOW)
        return title_modal_window.is_displayed()

    @allure.title('Проверка наличия номера заказа в списке всех заказов')
    def order_number_in_list(self, order_number):
        order_element = self.find_elements_with_wait(OrderFeedLocators.ORDER_FEED_LIST)

        for _ in order_element:
            order_element_text = self.get_text_from_element(OrderFeedLocators.ORDER_LIST_NUMBERS)
            if order_element_text == order_number:
                return True
            return False


    @allure.title('Получение номера счетчика выполненных заказов за все время')
    def get_all_time_counter_number(self):
        self.find_element_with_wait(OrderFeedLocators.ALL_TIME_COUNTER)
