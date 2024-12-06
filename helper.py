from selenium import webdriver
from selenium.webdriver.common.by import By
import random


class DataGeneration:
    @staticmethod
    def generate_random_name(minimum=2, maximum=12):
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        name = "".join(random.choice(characters) for _ in range(minimum, maximum))
        return name

    @staticmethod
    def generate_random_email(minimum=3, maximum=15):
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        email = "".join(random.choice(characters) for _ in range(minimum, maximum)) + f'@mail.ru'
        return email

    @staticmethod
    def generate_random_password(minimum=6, maximum=12):
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!№;%:?"
        password = "".join(random.choice(characters) for _ in range(minimum, maximum))
        return password

    @staticmethod
    def password_for_authorization():
        password = '123123'
        return password

    @staticmethod
    def email_for_authorization():
        email = 'korneev_14@gmail.ru'
        return email
