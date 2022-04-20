# Aleksandra Krišāne
# 18.04.2022

# 3. Web automatization/scraping project - Using Selenium
# read information from web page/s and save to some file format/database
# or perform some tasks on web page/s

# This script uses Selenium to scrape the data from the website
# https://www.ss.com/lv/ for the cars that were for sale in the selected time period.
# The data is then stored in a JSON file (max 30 cars).
# JSON file is used to get the list of cars that were for sale and
# to get the average car price, car with minimal run and lowest/highest priced car from the selection. Then,
# this new data can be saved to another JSON file by adding new lines in the end of the file.


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import json
from datetime import date
import time
from babel.numbers import format_currency  # for currency formatting


Color_Off = '\033[0m'   # Text Reset
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
UBlack='\033[4;30m'   # Black - Underline
IRed = '\033[0;91m'   # Red high intensity
BIYellow ='\033[1;93m'     # Bold Yellow high intensity
On_IBlue ='\033[0;104m'    # Blue high intensity background


todays_date = date.today()
current_time = time.strftime("%H:%M:%S")

s = Service("C:\Program Files\Python39\Scripts\chromedriver.exe")
driver = webdriver.Chrome(service=s)

url = "https://www.ss.com/lv/"
driver.get(url)
time.sleep(1)

cars_element = driver.find_element(by=By.ID, value="mtd_97")  # Vieglie auto
print(UNDERLINE + cars_element.text + ":" + Color_Off)  # Vieglie auto:
print(cars_element)

cars_element.click()
time.sleep(1)


def all_cars():
    all_cars_element = driver.find_elements(by=By.CLASS_NAME, value="a_category")
    vieglie_auto = []
    for car_element in all_cars_element:
        vieglie_auto.append(car_element.text)
        # print(i.text)
        if car_element.text == "Citas markas":  # -> mainās tabulas kolonnu skaits
            break
    return vieglie_auto


for car in all_cars():
    print("-> " + car)


def input_brand():
    brand = input("\nIzvēlieties marku: ")
    all_brands = all_cars()
    if brand.lower() == "exit":
        driver.close()
        exit()
    elif brand not in all_brands:
        print(IRed + "Ievadītā marka nav pieejama" + Color_Off)
        brand = input_brand()
    return brand


selected_car_model_input = input_brand()
selected_car_model = driver.find_element(by=By.LINK_TEXT, value=selected_car_model_input)

# print(selected_car_model.text)
selected_car_model.click()
time.sleep(1)

# select "Pārdod" from "Darījuma veids" dropdown
se2 = Select(driver.find_element(By.NAME, "sid"))
Select.select_by_visible_text(se2, "Pārdod")
time.sleep(1)


dropdown_elements = driver.find_elements(By.XPATH, value="//select[@id='today_cnt_sl']/option")
print("\nIevadiet vēlamo periodu: ")
i = 0  # indeksi sākas ar 0
for element in dropdown_elements:
    print(i, "-", element.text)
    i += 1


# getting index
def input_period():
    period = input("=> ")
    if period.lower() == "exit":
        driver.close()
        exit()
    elif period.isdigit() is False:
        print(IRed + "Ievadītais periods nav pieejams" + Color_Off)
        period = input_period()
    elif int(period) > len(dropdown_elements)-1:
        print(IRed + "Ievadītais periods nav pieejams" + Color_Off)
        period = input_period()
    elif int(period) < 0:
        print(IRed + "Ievadītais periods nav pieejams" + Color_Off)
        period = input_period()
    period = int(period)  # pirmais index ir 0
    return period


selection = input_period()

sel1 = Select(driver.find_element(By.ID, "today_cnt_sl"))

Select.select_by_index(sel1, selection)  # select by index (0-Visi Sludinājumi/1- Šodien/2 -Par 2 dienām/3 -Par 5 dienām)
time.sleep(1)


# get data from the first page only (newest, max 30 results)
cars_href = driver.find_elements(by=By.CLASS_NAME, value="am")  # all cars for sale from the first page
# get_all_links = [x.get_attribute("href") for x in cars_href if x.text != ""]  # get all links from the first page


# get car data from the first page table (max 30 cars)
cars_details = driver.find_elements(by=By.CLASS_NAME, value="amopt")
get_all_data = [x.text for x in cars_details if x.text != ""]  # get all car detail data from the first page


detailed_list_of_models = []
for i in range(0, int(len(get_all_data) / 5)):
    detailed_list_of_models.append({"marka": selected_car_model_input, "modelis": cars_details[i * 5].text,
                                    "gads": cars_details[i * 4 + i + 1].text, "tilpums": cars_details[i + 4 * i + 2].text,
                                    "nobraukums": cars_details[i + 4 * i + 3].text,
                                    "cena": cars_details[i + 4 * (i + 1)].text.strip(","),
                                    "href": cars_href[i].get_attribute("href")})


with open(f"car_data.json", "w", encoding="utf-8") as f:
    json.dump(detailed_list_of_models, f, ensure_ascii=False, indent=2, sort_keys=False)

driver.maximize_window()
driver.get_screenshot_as_file("top_cars_first_page.png")

# closing web page, all needed data is saved to json file
driver.close()


# to get the list of models
def available_unique_models():
    available_cars = open('car_data.json', 'r', encoding="utf-8")
    data = json.load(available_cars)
    total_len = len(data)
    if total_len == 0:
        print(IRed + "Šobrīd neviens modelis nav pieejams" + Color_Off)
        exit()
    n = 0
    list_of_models = []
    while n < total_len:
        if data[n]["modelis"] != "":
            if data[n]["modelis"] in list_of_models:
                pass
            else:
                list_of_models.append(data[n]["modelis"])
        n += 1
    return list_of_models


available_unique_models()


print(UBlack + f"Šobrīd pārdošanā ir sekojošie modeļi:" + Color_Off)  # \n{available_unique_models()}")
for i in available_unique_models():
    print("-> " + i)


def input_model():
    preferred_model = input("\nIzvēlieties modeli: ")
    if preferred_model.lower() == "exit":
        exit()
    elif preferred_model not in available_unique_models():
        print(IRed + "\nIevadītais modelis nav pieejams" + Color_Off)
        preferred_model = input_model()
    return preferred_model


model = input_model()


def search_for_model(model):
    all_models = open('car_data.json', 'r', encoding="utf-8")
    data = json.load(all_models)
    total_len = len(data)
    n = 0
    count = 0
    found_models = []
    auto_brand = data[0]["marka"]  # failā visas markas ir vienādas
    while n < total_len:
        if data[n]["modelis"] == model:
            count += 1
            found_models.append(f"{data[n]['marka']} {data[n]['modelis']} {data[n]['cena']} {data[n]['nobraukums']} {data[n]['href']}")
        n += 1
    brand_model = BOLD + f"{auto_brand} {model}" + Color_Off
    text_1 = f"\nŠobrīd ({todays_date.day}.{todays_date.month}.{todays_date.year}, {current_time}) pārdošanā"
    print(f"{text_1} ir {count} {brand_model} varianti: " if count > 1  # {auto_brand} {model}
          else f"Šodien ir pieejams tikai {count} {brand_model} variants:")  # {auto_brand} {model}
    for found_model_id in range(len(found_models)):
        print(found_model_id + 1, found_models[found_model_id])  # starts with 0, so i+1
    return found_models


search_for_model(model)


def avg_price(model):
    f = open('car_data.json', 'r', encoding="utf-8")
    data = json.load(f)
    total_len = len(data)
    n = 0
    count = 0
    summa = 0
    auto_brand = data[0]["marka"]  # failā visas markas ir vienādas
    while n < total_len:
        if data[n]["modelis"] == model:
            price = data[n]["cena"][:-2]
            price = price.replace(",", "")
            summa += float(price)
            count += 1
        n += 1
    avrg_price = round(summa / count, 2)
    # avrg_price = format_currency(avrg_price, 'EUR', locale='lv_LV', group_separator=True)  # nok due to issues like "6 350,00 € when saving to file"
    avrg_price = "{:.2f}".format(avrg_price) + " \u20ac"
    print(f"\n{auto_brand} {model} vidējā cena šobrīd ir : {avrg_price} ")  # \u20ac is euro sign
    return avrg_price


def cheapest_model_present(model):
    global cena
    f = open('car_data.json', 'r', encoding="utf-8")
    data = json.load(f)
    total_len = len(data)
    n = 0
    min_price = 0
    min_href = ""
    min_year = ""
    min_run = ""
    min_volume = ""
    auto_marka = data[0]["marka"]  # failā visas markas ir vienādas
    while n < total_len:
        if data[n]["modelis"] == model:
            price = data[n]["cena"][:-2]
            price = price.replace(",", "")
            if float(price) < min_price or min_price == 0:
                min_price = float(price)
                min_href = data[n]["href"]
                min_year = data[n]["gads"]
                min_run = data[n]["nobraukums"]
                min_volume = data[n]["tilpums"]
                cena = data[n]["cena"]  # due to formatting issues like "6 350,00 €"
        n += 1
    min_price = format_currency(min_price, 'EUR', locale='lv_LV', group_separator=True)
    print(f"\nLētākā {auto_marka} {model} cena šobrīd ir : {min_price}")  # \u20ac is euro sign
    print(UNDERLINE + "Detaļas:" + Color_Off)
    print(f" gads: {min_year}\n nobraukums: {min_run}\n tilpums: {min_volume}")
    print(f" sludinājums : {min_href}")
    min_price = cena  # due to formatting issues like "6 350,00 €"
    min_dataset = [{"Marka": auto_marka, "modelis": model, "gads": min_year, "nobraukums": min_run,
                    "tilpums": min_volume, "cena": min_price, "sludinājums": min_href}]
    return min_dataset


def most_expensive_model_present(model):
    global max_cena
    mem_data = open('car_data.json', 'r', encoding="utf-8")  # mem - most expensive model
    data = json.load(mem_data)
    total_len = len(data)
    n = 0
    max_price = 0
    max_href = ""
    max_year = ""
    max_run = ""
    max_volume = ""
    auto_marka = data[0]["marka"]  # failā visas markas ir vienādas
    while n < total_len:
        if data[n]["modelis"] == model:
            price = data[n]["cena"][:-2]
            price = price.replace(",", "")
            if float(price) > max_price:
                max_price = float(price)
                max_href = data[n]["href"]
                max_year = data[n]["gads"]
                max_run = data[n]["nobraukums"]
                max_volume = data[n]["tilpums"]
                max_cena = data[n]["cena"]  # due to formatting issues like "6 350,00 €"
        n += 1
    max_price = format_currency(max_price, 'EUR', locale='lv_LV', group_separator=True)
    print(f"\nDargākā {auto_marka} {model} cena šobrīd ir : {max_price}")  # \u20ac is euro sign
    print(UNDERLINE + "Detaļas:" + Color_Off)
    print(f" gads: {max_year}\n nobraukums: {max_run}\n tilpums: {max_volume}")
    print(f" sludinājums : {max_href}")
    max_price = max_cena  # due to formatting issues like "6 350,00 €"
    max_dataset = [{"Marka": auto_marka, "modelis": model, "gads": max_year, "nobraukums": max_run,
                    "tilpums": max_volume, "cena": max_price, "sludinājums": max_href}]
    return max_dataset


def min_run_present(model):
    min_run_data = open('car_data.json', 'r', encoding="utf-8")
    data = json.load(min_run_data)
    total_len = len(data)
    n = 0
    min_run = 0
    min_href = ""
    min_year = ""
    min_price = ""
    min_volume = ""
    auto_brand = data[0]["marka"]  # failā visas markas ir vienādas
    while n < total_len:
        if data[n]["modelis"] == model:
            run = data[n]["nobraukums"]
            if run == "-":
                run = -1
            else:
                run = data[n]["nobraukums"][:-7]
            if (float(run) < min_run or min_run == 0) and run != -1:
                min_run = float(run)
                min_href = data[n]["href"]
                min_year = data[n]["gads"]
                min_price = data[n]["cena"]
                min_volume = data[n]["tilpums"]
        n += 1
    min_run = str(f"{min_run:.0f} tūkst. km").format(min_run)
    print(f"\nMinimālais {auto_brand} {model} nobraukums šobrīd ir : {min_run}")
    print(UNDERLINE + "Detaļas:" + Color_Off)
    print(f" gads: {min_year}\n cena: {min_price}\n tilpums: {min_volume}\n nobraukums: {min_run}\n sludinājums : {min_href}")
    min_dataset = [{"Marka": auto_brand, "modelis": model, "gads": min_year, "nobraukums": min_run,
                    "tilpums": min_volume, "cena": min_price, "sludinājums": min_href}]
    return min_dataset


def save_to_file(*car_details, title="Dati:"):
    with open(f"saved_selected_car_data.json", "a", encoding="utf-8") as result_file:
        result_file.write("\n"+"_" * 100 + "\n")
        result_file.write(f"{todays_date.day}.{todays_date.month}.{todays_date.year}, {current_time}")
        result_file.write("\n")
        result_file.write(title)
        json.dump(car_details, result_file, ensure_ascii=False, indent=2, sort_keys=False)
        result_file.close()


# entering search criteria
# available_unique_models()
# model = input_model()
# search_for_model(model)

# functions
avg_price(model)
cheapest_model_present(model)
most_expensive_model_present(model)
min_run_present(model)


print("\n" + On_IBlue + BIYellow + "Failā tiks ierakstīta sekojoša informācija:" + Color_Off)
save_to_file(*search_for_model(model), title="Atlasītie sludinājumi:\n")
save_to_file(cheapest_model_present(model), title="Lētākais auto:\n")
save_to_file(most_expensive_model_present(model), title="Dargākais auto:\n")
save_to_file(min_run_present(model), title="Auto ar minimālo nobraukumu:\n")
save_to_file(avg_price(model), title="Vid. cena:\n")



from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import json
from datetime import date
import time

todays_date = date.today()
current_time = time.strftime("%H:%M:%S")

s = Service("C:\Program Files\Python39\Scripts\chromedriver.exe")
driver = webdriver.Chrome(service=s)

url = "https://www.ss.com/lv/"
driver.get(url)
time.sleep(1)

cars_element = driver.find_element(by=By.ID, value="mtd_180")  # kravas auto
print(cars_element.text + ":")  # kravas auto

cars_element.click()
time.sleep(1)

all_cars_element = driver.find_elements(by=By.CLASS_NAME, value="a_category")
kravas_auto = []
for i in all_cars_element:
    if i.text == "Citi":
        kravas_auto.append(i.text)
        break
    else:
        kravas_auto.append(i.text)

print(200 * "_")
print('kravas auto: by=By.CLASS_NAME, value="a_category"')
for i in kravas_auto:
    print(i)


elements = driver.find_elements(By.XPATH, value="//a[text()='Citi']")
for i in elements:
    print(i.text)
    i.click()
    time.sleep(10)
    driver.back()
    time.sleep(10)

elements = driver.find_elements(By.XPATH, value="//h4[@class='category']")
lists = []
for i in elements:
    if i.text.__contains__('Citi'):
        lists.append(i.text)
        break
    else:
        lists.append(i.text)

print(200 * "_")
print('kravas auto: by=By.XPATH, value="//h4[@class=\'category\']"')
for i in lists:
    print(i)

driver.quit()