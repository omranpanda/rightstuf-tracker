# rightstuf-tracker
Code that tracks the prices of things in rightstufanime and creates an image graph showing the change in price and sends it to you via email.


## Instructions

Just download all the files and add a URL from rightsufanime.com using the  run me python file.

run force recheck if you need to force the code to rerun otherwise just run the acp2.pyw
it will run in the  background and check every 24 hours. Add the acp.pyw to your startup so that it functions all the time without you having
to rerun it whenever you restart your computer

before running make sure to clear deh dates.csv file and add the folowing to the first line of the csv file: yyyymmdd of the previous day so for exmaple today is 2021/may/21st
so you would type this in the first line 20210520.
This should only be needed to be done once.

make sure to also add your email in the python files (both acp2 and force recheck) just do ctrl + f (coomand + f if on mac) and type email, you should find the places where you type in your email.

## Dependancies that are required to be installed

Python 3.0 +

matplotlib module 

numpy module

beautifulsoup4 module



