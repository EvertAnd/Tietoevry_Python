import time
from typing import List
import pandas as pd
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
direction_from = input("Ievadi sākuma adresi: ")
direction_to = input("Ievadi galamērķi: ")

driver = webdriver.Chrome("C:\Windows\Temp\chromedriver.exe")  # set path to chromedriver if you have no PATH
driver.set_window_size(1024, 600)
driver.maximize_window()
url = "https://www.bing.com/maps/directions"
driver.get(url)
# time.sleep(2)  # this will wait for 2 seconds

element = driver.find_elements(By.CLASS_NAME, "wayPointsContainer")
element = driver.find_elements(By.CLASS_NAME, "dirBtnGo commonButton")

driver.find_element(By.XPATH, '//*[@placeholder="From"]').send_keys(direction_from)
driver.find_element(By.XPATH, '//*[@placeholder="To"]').send_keys(direction_to)
pyautogui.press('enter')
time.sleep(2)  # this will wait for 2 seconds
pyautogui.press('Tab')
pyautogui.press('Enter')
pyautogui.press('Tab')
pyautogui.press('Enter')
