from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time




# Driver
driver = webdriver.Chrome()
driver.get("https://www.amazon.com.br/")
driver.maximize_window()

# look for searchbar
search_bar = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "twotabsearchtextbox"))
)
search_bar.click()
search_bar.send_keys("pc gamer completo")
search_bar.send_keys(Keys.RETURN)
time.sleep(5)

# items pricing
items_pricing_list = []
items_pricing = driver.find_elements(By.XPATH, "//span[@class='a-price']")
for items in items_pricing:
    try:
        items_pricing_list.append(items.text)
    except:
        items_pricing_list.append(None)

# items titles
items_titles_list = []
items_title = driver.find_elements(By.XPATH, "//h2[@class='a-size-base-plus a-spacing-none a-color-base a-text-normal']")
for items in items_title:
    items_titles_list.append(items.text)

## Web Scrapp dict
computadores = {
        'Titulo': items_titles_list,
        'Valor' : items_pricing_list
    }



computadores_df = pd.DataFrame(computadores)
computadores_csv = computadores_df.to_csv('computadores.csv')