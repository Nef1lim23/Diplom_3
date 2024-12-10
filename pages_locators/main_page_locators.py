from selenium.webdriver.common.by import By


class MainPageLocators:

    PERSONAL_ACCOUNT_BUTTON = By.XPATH, "//p[contains(text(),'Личный Кабинет')]"
    LOGIN_BUTTON = By.XPATH, "//button[contains(text(),'Войти в аккаунт')]"
    MAIN_PAGE_HEADER = By.XPATH, "//h1[contains(text(),'Соберите бургер')]"
    BUTTON_CREATE_ORDER = By.XPATH, "//button[contains(text(),'Оформить заказ')]"
