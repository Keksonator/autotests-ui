from playwright.sync_api import sync_playwright, expect

# Создание контекста
with sync_playwright() as playwright:
    # Запускаем Chromium браузер в обычном режиме (не headless)
    browser = playwright.chromium.launch(headless=False)
    # Создаем новый контекст браузера (новая сессия, которая изолирована от других)
    context = browser.new_context()
    # Открываем новую страницу в рамках контекста
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('username')

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    # Сохраняем состояние браузера (куки и localStorage) в файл для дальнейшего использования
    context.storage_state(path="browser-state.json")

# Открытие браузера в рамках созданного контекста
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")  # Указываем файл с сохраненным состоянием
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    # Проверка наличия заголовка страницы
    title = page.get_by_test_id("courses-list-toolbar-title-text")
    expect(title).to_have_text("Courses")

    # Проверка наличия иконки
    icon = page.get_by_test_id("courses-list-empty-view-icon")
    expect(icon).to_have_class("MuiSvgIcon-root MuiSvgIcon-fontSizeLarge css-il79at")

    # Проверка наличия названия блока
    block_title = page.get_by_test_id("courses-list-empty-view-title-text")
    expect(block_title).to_have_text("There is no results")

    # Проверка наличия текста в блоке
    block_text = page.get_by_test_id("courses-list-empty-view-description-text")
    expect(block_text).to_have_text("Results from the load test pipeline will be displayed here")

    print("Тест успешен")