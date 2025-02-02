import pytest
from selenium import webdriver
from selenium.webdriver.opera.service import Service
from selenium.webdriver.opera.options import Options

@pytest.mark.ui
def test_check_incorrect_username():
    # Вказуємо шлях до OperaDriver
    service = Service(executable_path=r'c://Users/pozna/furry-waddle/VitaliiTasik/operadriver.exe')
    
    # Налаштовуємо опції Opera
    opera_options = Options()
    opera_options.binary_location = r'c://Users/pozna/AppData/Local/Programs/Opera/launcher.exe'  # Шлях до виконуючого файлу Opera

    # Створення об'єкту для керування браузером
    driver = webdriver.Opera(service=service, options=opera_options)
    
    # Відкриваємо сторінку https://github.com/login
    driver.get("https://github.com/login")

    # Закриваємо браузер
    driver.quit()
