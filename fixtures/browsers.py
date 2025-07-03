import pytest  # Импортируем pytest
from playwright.sync_api import Playwright, \
    Page  # Имопртируем класс страницы, будем использовать его для аннотации типов


@pytest.fixture  # Объявляем фикстуру, по умолчанию скоуп function, то что нам нужно
def chromium_page(playwright: Playwright) -> Page:  # Аннотируем возвращаемое фикстурой значение
    # Запускаем браузер
    browser = playwright.chromium.launch(headless=False)
    # Передаем страницу для использования в тесте
    yield browser.new_page()
    # Закрываем браузер после выполнения тестов
    browser.close()


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    yield context.new_page()
    context.storage_state(path='browser-state.json')
    browser.close()


@pytest.fixture
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    yield context.new_page()
    browser.close()
