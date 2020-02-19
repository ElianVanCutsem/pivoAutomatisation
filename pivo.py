# this script can be used to make a reservation on the pivo website
# script written by Elian Van Cutsem

#imports
import time

# you need to install selenium for following imports
# pip install selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#variables
soiree = [
"Kleine PA-set met Midas",
"Lichtbrug van truss op 2 statieven, max 10m x 4m hoog",
"DJ-set Pioneer met CDJ2000",
"05.1.DDraadloze handmicrofoon",
"PC ADB C101 1000W",
"Wind-up Manfrotto 087",
"21..Spigot",
"13.ledspot",
"LED-sunstrips DMX",
"Blinder",
"Handdimmer 1 kanaal",
"Hazer",
"Fuif belichting op statief met LED-spots",
"SDI Kabelset met HDMI-omvormers",
"LCD-staander",
"Podiumelementen met losse pootjes",
"podiumpootjes 60cm",
"Db-meter",
"Set van 4 walkietalkies"
]

#functions
def getCredentials(i):
    readOut = []
    with open ('credentials.txt') as textFile:
        for line in textFile :
            readOut += line.rstrip("\n").split(" ")
        return readOut[i]

def login():
    login = getCredentials(0)
    password = getCredentials(1)
    loginElement = browser.find_element_by_id('username')
    loginElement.send_keys(login)
    passElement = browser.find_element_by_id('password')
    passElement.send_keys(password)
    passElement.submit()

def clearInput(webElement):
    webElement.send_keys(Keys.CONTROL + "a");
    webElement.send_keys(Keys.DELETE);

def addNewProduct(productToAdd):
    zoekTerm = browser.find_element_by_id('keyword')
    zoekTerm.send_keys(productToAdd)
    zoekTerm.submit()
    time.sleep(2)
    addButton = browser.find_elements_by_xpath('/html/body/div[2]/div[4]/div[1]/div[2]/div[1]/a[2]')[0]
    addButton.click()
    zoekTerm = browser.find_element_by_id('keyword')
    clearInput(zoekTerm)

def addItems(list):
    for x in range(0, len(list)):
        addNewProduct(list[x])

def doCheckup():
    reservationButton = browser.find_elements_by_xpath('/html/body/div[2]/div[3]/a')[0]
    reservationButton.click()

#running of program
# you need to install geckodriver for this
browser = webdriver.Firefox()
browser.get('https://www.vlaamsbrabant.be/promarUD/login.do')
login()
time.sleep(3)
addItems(soiree)
doCheckup()
