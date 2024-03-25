from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

# Parameters you can edit
search_text = "OpenAI"  # Example search text
number_of_searches = 5  # Total number of searches
total_duration_seconds = 60  # Total time to run the program in seconds

# Initialize WebDriver (Chrome in this case)
driver = webdriver.Chrome()

# Calculate interval between searches
if number_of_searches > 1:
    interval = total_duration_seconds / (number_of_searches - 1)
else:
    interval = total_duration_seconds

start_time = time.time()

for i in range(number_of_searches):
    if time.time() - start_time > total_duration_seconds:
        print("Total duration reached. Ending program.")
        break

    # Navigate to Google and perform the search
    driver.get("https://www.google.com")
    search_box = driver.find_element_by_name("q")
    search_box.send_keys(search_text + Keys.RETURN)

    # Wait for random time within the interval to mimic human behavior (optional)
    time_to_wait = interval + random.uniform(-10, 10)
    time.sleep(max(time_to_wait, 1))

driver.quit()
