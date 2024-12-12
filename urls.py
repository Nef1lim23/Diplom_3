#URLs

MAIN_PAGE = 'https://stellarburgers.nomoreparties.site/'

REGISTER_PAGE = f'{MAIN_PAGE}register'
LOGIN_PAGE = f'{MAIN_PAGE}login'
FORGOT_PASS_PAGE = f'{MAIN_PAGE}forgot-password'
RESET_PASS_PAGE = f'{MAIN_PAGE}reset-password'
PERSONAL_ACCOUNT_PAGE = f'{MAIN_PAGE}account/profile'
ORDER_HISTORY_PAGE = f'{MAIN_PAGE}account/order-history'
ORDER_FEED_PAGE = f'{MAIN_PAGE}feed'

#ENDPOINTS

BASE_URL = 'https://stellarburgers.nomoreparties.site/api/'
CREATE_USER_ENDPOINT = f'{BASE_URL}auth/register'
DELETE_USER_ENDPOINT = f'{BASE_URL}auth/user'
