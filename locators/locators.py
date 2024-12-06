from selenium.webdriver.common.by import By

LOGIN_BUTTON_XPATH = (By.XPATH, "//button[contains(text(),'Войти')]") # кнопка войти
EMAIL_INPUT_XPATH = (By.XPATH, "(//input[@name='name'])[1]") # поле ввода email
PASSWORD_INPUT_XPATH = (By.XPATH, "//input[@name='Пароль']") # поле ввода пароля
PERSONAL_CABINET_BUTTON_XPATH = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]") # кнопка для входа в личный кабинет
PERSONAL_CABINET_FORM_MAIN_XPATH = (By.XPATH, "(//div[@class='Account_contentBox__2CPm3'])[1]") # форма отображения личного кабинета
BUTTON_EXIT_XPATH = (By.XPATH, "//button[contains(text(),'Выход')]") # Кнопка выхода из ЛК
CONSTRUCTOR_TAB_LINK_XPATH = (By.XPATH, "//p[contains(text(),'Конструктор')]") # Кнопка перехода в конструктор
CONFIRM_ORDER_BUTTON_XPATH = (By.XPATH, "//button[contains(text(),'Оформить заказ')]") # кнопка оформления заказа
LOGO_BUTTON_XPATH = (By.XPATH, "(//*[name()='svg'])[3]") # Кнопка логотипа

# Страница конструктора

BUNS_SECTION = (By.XPATH, "//span[contains(text(),'Булки')]")  # Раздел "Булки"
SAUCES_SECTION = (By.XPATH, "//span[contains(text(),'Соусы')]")  # Раздел "Соусы"
TOPPINGS_SECTION = (By.XPATH, "//span[contains(text(),'Начинки')]")  # Раздел "Начинки"
BUNS_DIV = (By.XPATH, "//span[contains(text(),'Булки')]/parent::div")  # Контейнер раздела "Булки"
SAUCES_DIV = (By.XPATH, "//span[contains(text(),'Соусы')]/parent::div")  # Контейнер раздела "Соусы"
TOPPINGS_DIV = (By.XPATH, "//span[contains(text(),'Начинки')]/parent::div")  # Контейнер раздела "Начинки"

# Страница регистрации

NAME_INPUT_XPATH = (By.XPATH, '(//input[@name="name"])[1]') # Поле ввода имени
PASSWORD_INPUT_REGISTRATION_XPATH = (By.XPATH, '(//input[@name="Пароль"])[1]') # Поле ввода пароля
EMAIL_REGISTRATION_XPATH = (By.XPATH, '(//input[@name="name"])[2]') # Поле ввода Email для регистрации
BUTTON_REGISTRATION_XPATH = (By.XPATH, '(//button[contains(text(),"Зарегистрироваться")])[1]') # Кнопка "Зарегистрироваться"
MASSAGE_IS_AN_INCORRECT_PASSWORD = (By.XPATH, "//p[@class='input__error text_type_main-default']") # Сообщение об ошибке при неправильном пароле

#Страница авторизации

SUBMIT_LOGIN_BUTTON_XPATH = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]") # Кнопка войти в аккаунт
ORDER_BUTTON_TEXT_XPATH = (By.XPATH, "//button[contains(text(),'Оформить заказ')]") # Кнопка Оформить заказ
OPEN_LOGIN_PAGE_LINK_XPATH = (By.XPATH, "//a[contains(text(),'Войти')]") # Кнока войти
PASSWORD_RECOVERY_XPATH = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]") # Кнопка восстановления пароля
ENTRY_FORM_XPATH = (By.XPATH, "//div[@class='Auth_login__3hAey']") # Форма авторизации