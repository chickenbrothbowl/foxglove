from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui
import time
import random

driver = webdriver.Chrome()
driver.get("https://www.instagram.com/accounts/login/") 

input("Press Enter after login to begin")
mode = input("(S)croll mode or (L)ike mode? ").strip().upper()
interactions = int(input("Enter number of interactions: "))

topic = input("Enter topic: ").strip().lstrip("#")
driver.get("https://www.instagram.com/explore/search/keyword/?q=" + topic)

time.sleep(5)

# scroll a bit to load
driver.execute_script("window.scrollTo(0, 500);")
time.sleep(3)

for _ in range(interactions):
    try:
        post_links = driver.find_elements(By.XPATH, '//a[contains(@href, "/p/")]')
        if not post_links:
            print("No posts found.") # only empty topics or end of topic
            continue

        random_post = random.choice(post_links)
        driver.execute_script("arguments[0].scrollIntoView(true);", random_post)
        time.sleep(random.uniform(1, 2))
        random_post.click()
        time.sleep(random.uniform(2, 3))

        if mode == "L" or mode == "LIKE":
            pyautogui.doubleClick(x=500, y=500)
            time.sleep(random.uniform(1, 2))

        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)

    except Exception as e:
        #print("Error during interaction:", e) # debugging
        print("")

    time.sleep(random.uniform(2, 3))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(random.uniform(2, 3))

driver.quit()