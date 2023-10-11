import pytest
import requests
import time


@pytest.mark.parametrize('url', ['https://rt-internet.ru/'])  # Использование декоратора parametrize для параметризации теста
def test_page_load_time(url):  # Определение функции теста для измерения времени загрузки страницы
    start_time = time.time()  # Засечка времени начала загрузки страницы
    response = requests.get(url)  # Отправка HTTP-запроса GET на указанный URL
    elapsed_time = time.time() - start_time  # Вычисление затраченного времени на загрузку страницы


    # Проверка статуса ответа (должен быть 200 OK)
    assert response.status_code == 200, f"Ошибка: получен статус {response.status_code}"

    # Проверка времени загрузки страницы
    assert elapsed_time < 2, f"Ошибка: время загрузки страницы составляет {elapsed_time:.2f} секунд"

    print(f"Страница {url} загружена за {elapsed_time:.2f} секунд.")
