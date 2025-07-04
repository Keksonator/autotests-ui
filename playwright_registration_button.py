from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу входа
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Проверяем, что кнопка Login не активна
    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_disabled()

    # Вводим email
    email_input = page.get_by_test_id("registration-form-email-input").locator("input")
    email_input.fill("user.name@gmail.com")

    # Вводим логин
    username_input = page.get_by_test_id("registration-form-username-input").locator("input")
    username_input.fill("username")

    # Вводим пароль
    password_input = page.get_by_test_id("registration-form-password-input").locator("input")
    password_input.fill("password")

    # Проверяем, что кнопка активна
    expect(registration_button).to_be_enabled()
    print("Тест успешен")