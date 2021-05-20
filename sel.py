# Hey guys let's connect via LinkedIn
# How? Just past this entire message in a .py file in your IDE (VS Code, PyCharm..) and run it
# Just make sure you install 'Python' before that 'https://www.python.org/downloads/'
# Also, go on your 'Command Prompt' and run 'pip install selenium && pip install webdriver_manager && pip install tinydb'
# And we're good to go, just run the file in an IDE
import os
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir={}\driver_data".format(os.getcwd()))

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

driver.get("https://linkedin.com")

try:
    driver.get("https://www.linkedin.com/in/gauravjnu/")
    print("accessing link")
    sleep(3)
    el=driver.find_element_by_xpath("//button[@class='pvs-profile-actions__action artdeco-button artdeco-button--2 artdeco-button--primary ember-view']")
    el.click()

    sendButton = None
    sendButton=driver.find_element_by_xpath("//button[@class='ml1 artdeco-button artdeco-button--3 artdeco-button--primary ember-view']")
    if sendButton:
        sendButton.click()

except Exception as e:
    print("error processing link\nlink: ", link, "\nerror",  e)
