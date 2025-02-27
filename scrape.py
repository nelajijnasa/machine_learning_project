from selenium import webdriver
import time
import csv
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the IUCN Red List page
driver.get("https://www.iucnredlist.org/search/grid?taxonLevel=Amazing&searchType=species")
time.sleep(2)

# Perform search
driver.find_element(By.XPATH, "//input[@class='search search--site']").send_keys("animals")
driver.find_element(By.XPATH, "//button[@class='search--site__button search-form-button']").click()
time.sleep(3)

# Extract species information
species_data = []
species_list = driver.find_elements(By.XPATH, "//a[@class='link--faux']")

for species in species_list:
    link_url = species.get_attribute("href")
    driver.execute_script("window.open(arguments[0],'_blank');", link_url)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(3)

    try:
        name = driver.find_element(By.XPATH, "//h1").text
        habitat = driver.find_element(By.XPATH, "(//section[@id='habitat-ecology']//p)[1]").text
        threats = driver.find_element(By.XPATH, "(//section[@id='threats']//p)[1]").text
        population_trend = driver.find_element(By.XPATH, "//span[@class='label' and text()='Population Trend']/following-sibling::span").text
        category_status = driver.find_element(By.XPATH, "//span[@class='label' and text()='Category']/following-sibling::span").text
        category = driver.find_element(By.XPATH, "//span[@class='label' and text()='Class']/following-sibling::span").text
        generation_length = driver.find_element(By.XPATH, "(//section[@id='habitat-ecology']//p)[2]").text

        species_data.append([name, habitat, threats, population_trend, category_status, category, generation_length])

    except NoSuchElementException:
        pass

    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)

# Save data to CSV
with open('data/species_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["NAMES", "HABITAT", "NO_OF_THREATS", "POPULATION_TREND", "CATEGORY_STATUS", "CATEGORY", "GENERATION_LENGTH"])
    writer.writerows(species_data)

driver.quit()
