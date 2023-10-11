import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    # Инициализация веб-драйвера
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_faq_page(driver):
    # Открыть сайт Ростелеком
    driver.get("https://rt-internet.ru/")

    # Переход на страницу FAQ
    driver.get("https://rt-internet.ru/faq")

    # Ожидание загрузки страницы FAQ (например, ожидание появления первого вопроса)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "summary"))
    )

    # Сбор всех вопросов на странице FAQ
    questions = driver.find_elements(By.CSS_SELECTOR, "summary")
    assert len(questions) > 0, "Вопросы отсутствуют на странице FAQ"

    # Сбор всех ответов на странице FAQ
    answers = driver.find_elements(By.CSS_SELECTOR, "p")
    assert len(answers) > 0, "Ответы отсутствуют на странице FAQ"

    # Вывод сообщения, что на странице FAQ присутствуют вопросы и ответы
    print(f"На странице FAQ присутствуют {len(questions)} вопросов и {len(answers)} ответов.")
