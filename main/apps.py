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


        thread = threading.Thread(target=scrapingscheduler)
        thread.start()