from django.apps import AppConfig
import sys

#SOLUTION TO RUN CODE, HOWEVER I'M USING ANOTHER SOLUTION AT WSGI FILE


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

# SOLUTION TO RUN CODE, HOWEVER I'M USING ANOTHER SOLUTION AT WSGI FILE

    # pra fazer funcionar é só tirar os comentarios
    def ready(self):
        from backendfunctions import scrapingscheduler
        import threading
        from track.models import Track
        from .models import CustomUser
        thread = threading.Thread(target=scrapingscheduler)
        thread.start()