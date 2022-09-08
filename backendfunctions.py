from django.core.mail import send_mail
import smtplib
import threading
import os
from apscheduler.schedulers.blocking import BlockingScheduler
from track.models import Track
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import datetime


def send_email_confirmation(form):
    # form.instance.user = self.request.user
    # if form.instance.user:
    send_mail('Welcome to Track Price', f'Dear, {form.cleaned_data["username"]}.\n\nWelcome to Track Price. \n\nWe hope you may enjoy our tool.\n\nLink: https://pricetrackdjango.herokuapp.com/\n\nAtt, team.', 'trackpricedjango@gmail.com', [form.cleaned_data['email']],fail_silently=False)




def send_email_price(email,desired_price, price, name,user,link):
    send_mail(f'{name} below R$ {desired_price}!!! ',f'Dear, {user}.\n\nThe price of {name} is R$ {price}.\n\nIt is below the one you set as desired (R$ {desired_price})\n\nI suggest you run in order not to miss the chance. \n\n Item link: {link}\n\nAtt, Track Price team.','trackpricedjango@gmail.com', [email], fail_silently=False)

def scraping(link): #function to perform scrapping
    navegador = webdriver.Chrome()
    navegador.get(link)
    try:
        if 'amazon.com.br/' in link:
            if link == 'https://www.amazon.com.br/':
                return None
            elemento = float(navegador.find_element(By.XPATH, '//*[@id="corePrice_feature_div"]/div/span/span[2]/span[2]').text.replace(".",""))
            return elemento

        elif "mercadolivre.com.br/" in link: #mercadolivre has two different kind of pages.
            if link == 'https://www.mercadolivre.com.br/':
                return None
            try:
                elemento=float(navegador.find_element(By.XPATH,'//*[@id="price"]/div/div[1]/span/span[3]').text.replace(".","").replace(",","."))
                return elemento
            except:
                elemento = float(navegador.find_element(By.XPATH, '//*[@id="ui-pdp-main-container"]/div[1]/div/div[1]/div[2]/div[3]/div[1]/span[1]/span[3]').text.replace(".","").replace(",","."))
                return elemento

        elif 'magazineluiza.com.br/' in link: #magazine has a differente way when the product is on sale the xpath is different
            if link == 'https://www.magazineluiza.com.br/':
                return None
            try:#first I check if xpathp[3] exists, if it exists price is xpath p[2], if it doesn't price is xpath p[1]
                elemento = navegador.find_element(By.XPATH, '//*[@id="__next"]/div/main/section[4]/div[4]/div/div/div/p[3]').text.strip("R$ ").replace(".","").replace(",",".")
                elemento = navegador.find_element(By.XPATH,'//*[@id="__next"]/div/main/section[4]/div[4]/div/div/div/p[2]').text.strip("R$ ").replace(".","").replace(",",".")
                return float(elemento)
            except:
                elemento = navegador.find_element(By.XPATH,'//*[@id="__next"]/div/main/section[4]/div[4]/div/div/div/p[1]').text.strip("R$ ").replace(".","").replace(",",".")
                print(elemento)
                return float(elemento)


        elif 'americanas.com.br' in link: #americanas has a differente way when the product is on sale the xpath is different
            if link == 'https://www.americanas.com.br/':
                return None
            elemento = navegador.find_element(By.XPATH, '//*[@id="rsyswpsdk"]/div/main/div[2]/div[2]/div[1]/div[2]/div').text.strip("R$ ").replace(".","").replace(",",".")
            if elemento == "":
                elemento = navegador.find_element(By.XPATH,'//*[@id="rsyswpsdk"]/div/main/div[2]/div[2]/div[1]/div[1]/div').text.strip("R$ ").replace(".", "").replace(",", ".")
                return float(elemento)
            return float(elemento)

        else:
            return None
    except:
        return None

def updatescraping(Track):
    objects = Track.objects.all()
    for object in objects:
        value = scraping(object.url)
        data = object.prices['data']
        date = datetime.now() #get current data and hour
        first_string = date.strftime("%B %d, %Y %A, %H:%M:%S") #make it string format

        new_data = [first_string,value]
        data.append(new_data)
        object.prices['data'] = data
        object.save()
        if value == None: #if para evitar erro de comparar null com float
            value = 100000000
        if value<=object.desired_price:
            send_email_price(object.user.email,object.desired_price,value,object.name,object.user,object.url)

def waiting():
    for i in range(10000):
        print(i)

def scrapingscheduler():  #function to run the scraping in intervals
    scheduler = BlockingScheduler()
    scheduler.add_job(lambda: updatescraping(Track), 'interval', seconds=15)
    scheduler.start()

# def scrapingscheduler2():  # function to run the scraping in intervals
#     scheduler = BlockingScheduler()
#     scheduler.add_job(waiting, 'interval', seconds=5)
#     scheduler.start()
