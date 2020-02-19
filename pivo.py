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

#running of program
# you need to install geckodriver for this
browser = webdriver.Firefox()
browser.get('https://www.vlaamsbrabant.be/promarUD/login.do')
login()
