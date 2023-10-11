import pytest
import requests
import time


@pytest.mark.parametrize('url', ['https://rt-internet.ru/'])
def test_page_load_time(url):
    start_time = time.time()
    response = requests.get(url)
    elapsed_time = time.time() - start_time

    # Проверка статуса ответа (должен быть 200 OK)
    assert response.status_code == 200, f"Ошибка: получен статус {response.status_code}"

    # Проверка времени загрузки страницы
    assert elapsed_time < 2, f"Ошибка: время загрузки страницы составляет {elapsed_time:.2f} секунд"

    print(f"Страница {url} загружена за {elapsed_time:.2f} секунд.")
