from django.apps import AppConfig
import sys
import threading

#SOLUTION TO RUN CODE, HOWEVER I'M USING ANOTHER SOLUTION AT WSGI FILE
#def waiting():
   #for i in range(2000):
       #print(i)



class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

#SOLUTION TO RUN CODE, HOWEVER I'M USING ANOTHER SOLUTION AT WSGI FILE

    #def ready(self):
        #if 'runserver' not in sys.argv:
            #return True

        #thread = threading.Thread(target=waiting)
        #thread.start()