# теория
# скрипт скроллит страницу до элемента button

import time

from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element(By.TAG_NAME, "button")
time.sleep(1)
# js-скрипт для скролла
browser.execute_script(
    "return arguments[0].scrollIntoView({block: 'start', inline: 'nearest', behavior: 'smooth'});",
    button,
)
time.sleep(2)
button.click()