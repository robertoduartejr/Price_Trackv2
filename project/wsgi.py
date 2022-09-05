"""
WSGI config for project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""
import threading
import os
from apscheduler.schedulers.blocking import BlockingScheduler
from track.models import Track
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import datetime
from backendfunctions import send_email_price,scrapingscheduler,scraping,updatescraping

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

#SOLUTION TO RUN CODE SHOULD BE WRITTEN HERE


thread = threading.Thread(target=scrapingscheduler)
thread.start()
#SOLUTION TO RUN CODE SHOULD BE WRITTEN HERE

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
