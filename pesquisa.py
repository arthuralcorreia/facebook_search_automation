from bs4 import BeautifulSoup
import requests
from selenium import webdriver

email = input("Insira aqui seu e-mail")
senha = input("insira aqui sua senha")

browser = webdriver.Firefox()

def login():   
    browser.get('https://www.facebook.com/')
    python_button = browser.find_element_by_xpath('//*[@id="email"]')
    python_button.send_keys(email)
    python_button = browser.find_element_by_xpath('//*[@id="pass"]')
    python_button.send_keys(senha)
    python_button = browser.find_element_by_xpath('//*[@id="u_0_2"]')
    python_button.click()

def lista():
    browser.get("https://www.facebook.com/"

login()
lista()
