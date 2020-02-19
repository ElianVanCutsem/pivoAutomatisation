# script written by Elian Van Cutsem

#imports
import time
# you need to install selenium for this
from selenium import webdriver

#variables
login = ""
password = ""

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

def addNewProduct(productToAdd):
    zoekTerm = browser.find_element_by_id('keyword')
    zoekTerm.send_keys(productToAdd)
    zoekTerm.submit()
    time.sleep(1)
    print(browser.find_elements_by_xpath('/html/body/div[2]/div[4]/div[1]/div[2]/div[1]/a[2]'))
    addButton = browser.find_elements_by_xpath('/html/body/div[2]/div[4]/div[1]/div[2]/div[1]/a[2]')[0]
    addButton.click()

#running of program
# you need to install geckodriver for this
browser = webdriver.Firefox()
browser.get('https://www.vlaamsbrabant.be/promarUD/login.do')
login()
time.sleep(3)
addNewProduct("XLR kabelset 10stuks van 10m in koffer")
