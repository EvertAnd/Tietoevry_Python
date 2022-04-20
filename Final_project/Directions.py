import pyautogui
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
import json
from datetime import date
import time

direction_from = input("Ievadi sākuma adresi: ")
direction_to = input("Ievadi galamērķi: ")

s = Service("C:\Program Files\Python39\Scripts\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.set_window_size(1024, 600)
driver.maximize_window()
url = "https://www.bing.com/maps/directions"
driver.get(url)

time.sleep(2)  # this will wait for 2 seconds

element = driver.find_elements(By.CLASS_NAME, "wayPointsContainer")
element = driver.find_elements(By.CLASS_NAME, "dirBtnGo commonButton")
element = driver.find_elements(By.CLASS_NAME, "directionsPanelRoot")

driver.find_element(By.XPATH, '//*[@class="dirBtnDrive dirBtnNormal"]').click()  #Nospiež opciju braukt ar mašīnu (Var izdomāt izvēlēties Auto vai ar k'ājām. ??


driver.find_element(By.XPATH, '//*[@placeholder="From"]').send_keys(direction_from)
driver.find_element(By.XPATH, '//*[@placeholder="To"]').send_keys(direction_to)
pyautogui.press('enter')
time.sleep(2)

title = driver.find_element(By.CLASS_NAME, "title")  # Atrod meklētās norādes nosaukums veidojas no "from" to "To"
print(title.text)


driver.get_screenshot_as_file("The_way.png")
time.sleep(2)  # this will wait for 2 seconds
pyautogui.press('Tab')
pyautogui.press('Enter')

def all_dir():
    allldir = driver.find_elements(By.CLASS_NAME, "bm_dirInstructionRow")
    directions = []
    for element in allldir:
        directions.append(element.text)
    return directions


for dir in all_dir():
    print("-> " + dir)
