from django.apps import AppConfig
import sys
import threading
from apscheduler.schedulers.blocking import BlockingScheduler

#SOLUTION TO RUN CODE, HOWEVER I'M USING ANOTHER SOLUTION AT WSGI FILE
def waiting():
   for i in range(2000):
       print(i)

def scrapingscheduler2():  # function to run the scraping in intervals
    scheduler = BlockingScheduler()
    scheduler.add_job(waiting, 'interval', seconds=5)
    scheduler.start()


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

#SOLUTION TO RUN CODE, HOWEVER I'M USING ANOTHER SOLUTION AT WSGI FILE

    def ready(self):
        if 'runserver' not in sys.argv:
            return True

        thread = threading.Thread(target=scrapingscheduler2)
        thread.start()