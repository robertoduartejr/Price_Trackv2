from django.apps import AppConfig
import sys

#SOLUTION TO RUN CODE, HOWEVER I'M USING ANOTHER SOLUTION AT WSGI FILE


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

#SOLUTION TO RUN CODE, HOWEVER I'M USING ANOTHER SOLUTION AT WSGI FILE

    def ready(self):
        if 'runserver' not in sys.argv:
            return True

        from backendfunctions import scrapingscheduler
        import threading
        from selenium import webdriver
        import os

        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

        thread = threading.Thread(target=scrapingscheduler)
        thread.start()