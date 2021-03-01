import matplotlib.pyplot as plt
import numpy as np
import datetime
import csv
import requests
from bs4 import BeautifulSoup
import matplotlib.ticker as ticker
import matplotlib.dates as mdates
import time
import os

def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open("data/" + file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = csv.writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

def date_id(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = csv.writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow([list_of_elem])

def predef(file_name, price):
    # Open file in append mode
    with open("data/" + file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = csv.writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(['Date,Price ($)'])

    inttoday = int(today)
    inttoday -= 1
    oldday = str(inttoday)
    finalstr = oldday + ',' + str(price)
    print(finalstr)

    leto = [oldday,str(price)]



    with open("data/" + file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = csv.writer(write_obj)
        # Add contents of list as last row in the csv file

        csv_writer.writerow(leto)




def check():

    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 OPR/73.0.3856.284'}

#    with open('URLs.csv', 'r') as read_url:
#        URLs = csv.reader(read_url)
#        url_list = list(URLs)
#    URL_str = [''.join(u) for u in url_list]

    if not os.path.exists('images'):
        os.makedirs('images')

    if not os.path.exists('data'):
        os.makedirs('data')


    for urlt in URL_str:


        URL = urlt

        page = requests.get(URL, headers = headers)

        soup = BeautifulSoup(page.content, "html.parser")

        title = soup.find(class_="product-details-full-content-header-title").get_text()

        priceOG = soup.find(class_="product-views-price-old").get_text()

        convertedOG = float(priceOG[1:])

        priceNew = soup.find(class_="product-views-price-lead sezzle-min").get_text()

        converted = float(priceNew[1:])



        today = datetime.date.today()
        today = str(today)
        today = today.replace("-", "")

        try:
            f = open("data/" + title + ".csv")
            f.close()
        except:
            predef(title + ".csv", convertedOG)

        list = [today,converted]

        append_list_as_row(title + ".csv", list)


        dates,cost = np.loadtxt("data/" + title + '.csv',delimiter=',',skiprows=1,unpack=True)

        xdates = [datetime.datetime.strptime('{:08}'.format(int(date)),'%Y%m%d') for date in dates]





        fig = plt.figure()
        ax = plt.subplot(111)
        formatter = ticker.FormatStrFormatter('$%1.2f')
        ax.yaxis.set_major_formatter(formatter)

        plt.plot(xdates, cost,'o-',label=title, lw = 3)
        plt.yticks(np.arange(5, max(cost+10), 3))

        plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), fancybox=True, shadow=True, ncol=5)
        plt.ylabel('Price (USD)')
        plt.xlabel('Deh Date')
        plt.gcf().autofmt_xdate()
        plt.grid()

        plt.gca().xaxis.set_major_locator(mdates.DayLocator())
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))

        plt.savefig("images/" + title + '.png')


        import smtplib
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart
        from email.mime.base import MIMEBase
        from email import encoders

        email_user = 'the email that sends the image'
        email_password = 'emailpassword'
        email_send = 'the email that gets the image'

        subject = title + ' - Price Watch'

        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = email_send
        msg['Subject'] = subject

        body = " "
        msg.attach(MIMEText(body,'plain'))

        filename= "images/" + title + '.png'
        attachment  =open(filename,'rb')

        part = MIMEBase('application','octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',"attachment; filename= "+filename)

        msg.attach(part)
        text = msg.as_string()
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(email_user,email_password)


        server.sendmail(email_user,email_send,text)
        server.quit()







while True:
    try:
        f = open("dates.csv")
        f.close()
    except:
        today = datetime.date.today()
        today = str(today)
        today = today.replace("-", "")
        today = int(today)
        today -= 1
        today = str(today)
        date_id("dates.csv", today)


    with open('dates.csv', "r") as f1:
        last_line = f1.readlines()[-1]
    d = (last_line[0:8])
    today = datetime.date.today()
    today = str(today)
    today = today.replace("-", "")
    with open('URLs.csv', 'r') as read_url:
        URLs = csv.reader(read_url)
        url_list = list(URLs)
    URL_str = [''.join(u) for u in url_list]
    check()
    date_id("dates.csv", today)
    print("Forced recheck, process completed and will recheck in 24 hours")
    time.sleep(60*60*24)
