from playwright.sync_api import sync_playwright, expect, Page
import pytest
from pages.login_page import LoginPage  # Импортируем LoginPage


@pytest.mark.regression
@pytest.mark.authorization
@pytest.mark.parametrize("email, password", [
    ("user.name@gmail.com", "password"),
    ("user.name@gmail.com", "  "),
    (" ", "password"),
]
                         )
def test_wrong_email_or_password_authorization(login_page: LoginPage, email: str,
                                               password: str):  # Создаем тестовую функцию

    login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    # Заполняем форму авторизации
    login_page.fill_login_form(email=email, password=password)
    # Нажимаем кнопку "Login"
    login_page.click_login_button()
    # Проверяем наличие сообщения об ошибке
    login_page.check_visible_wrong_email_or_password_alert()


#python -m pytest -k "test_wrong_email_or_password_authorization" -s -v