# script written by Elian Van Cutsem

#imports
import webbrowser
#from selenium import webdriver

#start of program
#webbrowser.open('http://www.google.com')

#variables
login = ""
password = ""

def getCredentials():
    readOut = []
    with open ('credentials.txt') as textFile:
        for line in textFile :
            readOut += line.rstrip("\n").split(" ")
        login = readOut[0]
        password = readOut[1]

getCredentials()
