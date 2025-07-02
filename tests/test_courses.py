from playwright.sync_api import sync_playwright, expect
import pytest


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    # Проверка наличия заголовка страницы
    title = chromium_page_with_state.get_by_test_id("courses-list-toolbar-title-text")
    expect(title).to_have_text("Courses")

    # Проверка наличия иконки
    icon = chromium_page_with_state.get_by_test_id("courses-list-empty-view-icon")
    expect(icon).to_have_class("MuiSvgIcon-root MuiSvgIcon-fontSizeLarge css-il79at")

    # Проверка наличия названия блока
    block_title = chromium_page_with_state.get_by_test_id("courses-list-empty-view-title-text")
    expect(block_title).to_have_text("There is no results")

    # Проверка наличия текста в блоке
    block_text = chromium_page_with_state.get_by_test_id("courses-list-empty-view-description-text")
    expect(block_text).to_have_text("Results from the load test pipeline will be displayed here")

    print("Тест успешен")
