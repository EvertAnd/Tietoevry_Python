import pyautogui
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
from itertools import zip_longest
import json
from datetime import date
import time


# Var  izvēlēties Auto vai ar kājām. ?? ( Jāpieestrādā, jo neiet tālāk pēc šī. )
def metodetogetto():
    metodetoget = input("Ievadiet vēlāmo pārvietošanās metodi. Auto -"'A'", Kājām - "'K'": ")
    all_metods = 'dirBtnDrive dirBtnNormal', 'dirBtnWalk dirBtnNormal'
    if metodetoget == "A":
        way = "dirBtnDrive dirBtnNormal"
        return way
    if metodetoget == "K":
        way = "dirBtnWalk dirBtnNormal"
        return way
    if metodetoget not in all_metods:
        print(metodetoget + " Ievadītā opcija nav pieejama")
        way = metodetogetto()
    return way


selectemetod = metodetogetto()
print(selectemetod)

direction_from = input("Ievadi sākuma adresi: ")
direction_to = input("Ievadi galamērķi: ")

s = Service("C:\\Program Files\\Python39\\Scripts\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.set_window_size(1024, 600)
driver.maximize_window()
url = "https://www.bing.com/maps/directions"
driver.get(url)

element = driver.find_elements(By.CLASS_NAME, "wayPointsContainer")
# element = driver.find_element(By.XPATH, '//*[@class="wayPointsContainer"]')
element = driver.find_elements(By.CLASS_NAME, "directionsPanelRoot")
element = driver.find_elements(By.CLASS_NAME, "dirBtnGo commonButton")
element = driver.find_elements(By.CLASS_NAME, "dirModes")
element = driver.find_elements(By.CLASS_NAME, "dirTopRow")
time.sleep(1)  # this will wait for 1 seconds

driver.find_element(By.XPATH, '//*[@class="dirBtnWalk dirBtnNormal"]').click()  # Nospiež opciju braukt ar mašīnu (ok)
# driver.find_element(By.CLASS_NAME, selectemetod).click()
# selected_way = driver.find_element(By.CLASS_NAME, value=selectemetod)  # Sākuma izvēlne Auto vai ar Kājām (nok)
# selected_way.click()  # Nospiež opciju braukt ar mašīnu   (Nok)

# driver.find_element(by=By.CLASS_NAME, value="dirBtnDrive dirBtnNormal").click() # variants (nok)
# driver.find_element(By.CLASS_NAME, value=selectemetod).click()
# selected_way.click()  # Nospiež opciju braukt ar mašīnu   (Nok)

time.sleep(1)  # this will wait for 1 seconds
driver.find_element(By.XPATH, '//*[@placeholder="From"]').send_keys(direction_from)
driver.find_element(By.XPATH, '//*[@placeholder="To"]').send_keys(direction_to)
# driver.find_element(By.XPATH, '//*[@placeholder="To"]').send_keys(direction_next)

time.sleep(1)
pyautogui.press('enter')
time.sleep(2)

title = driver.find_element(By.CLASS_NAME, "title")  # Atrod meklētās norādes nosaukums veidojas no "from" to "To"
print(title.text)

driver.get_screenshot_as_file("The_way.png")
time.sleep(2)  # this will wait for 2 seconds
pyautogui.press('Tab')
pyautogui.press('Enter')


def all_dir():
    dirInstruction = driver.find_elements(By.CLASS_NAME, "dirInstruction")
    directions = []
    for elemento in dirInstruction:
        directions.append(elemento.text)
    directions = [x for x in directions if x]
    return directions


def all_dist():
    travelDist = driver.find_elements(By.CLASS_NAME, "dirInstructionTravelDistance")
    distances = ['0 km']
    for element in travelDist:
        distances.append(element.text)
    distances = [x for x in distances if x]
    return distances


def replace_none_values(some_dict):
    return {k: ('' if v is None else v) for k, v in some_dict.items()}


interm_route = zip_longest(all_dir(), all_dist())
final_route = replace_none_values(dict(interm_route))


for key, value in final_route.items():
    print(key, '-', value)

