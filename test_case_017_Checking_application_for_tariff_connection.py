import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture  # Определение фикстуры для инициализации и завершения работы драйвера
def driver():
    driver = webdriver.Chrome()  # Создание экземпляра драйвера Chrome
    yield driver  # Возврат драйвера тестовой функции и ожидание завершения теста
    driver.quit()  # Закрытие браузера после завершения теста


def test_game_tariff_application(driver):
    driver.get("https://rt-internet.ru/")

    # Находим тариф “Игровой” и нажимаем кнопку подключить
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#b10419 > div > div:nth-child(2) > div:nth-child(1) > a"))
    )
    driver.execute_script("arguments[0].click();", element)

    # Заполняем поля заявки
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#b12674 > input"))).send_keys(
        "Литвинов Владимир Сергеевич")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#b12675 > input"))).send_keys("Москва")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#b12677 > input"))).send_keys("Тверская")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#b12678 > input"))).send_keys("10")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#b12679 > input"))).send_keys("20")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#b12680 > input"))).send_keys("9123456789")

    # Ставим галочку
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#fields\\.174870"))).click()

    # Нажимаем кнопку Оформить заявку
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#b12683"))).click()

    # Проверяем, что заявка оформлена успешно
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#c_538"), "Ваша заявка принята"))
