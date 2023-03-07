from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select



from selenium.webdriver.common.keys import Keys
import os

import time
import sys

l1 = []
filename = sys.argv[1]
with open(filename) as f:
    while True:
        line = f.readline()
        if not line:
            break
        l1.append(line.strip())

userid = l1[0]
pas = l1[1]

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.minimize_window()

driver.get("https://kiitportal.kiituniversity.net/irj/portal/")
driver.implicitly_wait(10)

ids = driver.find_elements(By.ID, "logonuidfield")


id = driver.find_element(By.XPATH, "//input[@id='logonuidfield']").send_keys(userid)
password = driver.find_element(By.ID, 'logonpassfield').send_keys(pas)
login = driver.find_element(By.XPATH, "//input[@class='urBtnStdNew']").click()
driver.find_element(By.LINK_TEXT,
                    'Student Self Service for Computer Science & Systems Engineering (CSSE - 2020 Batch)').click()
# driver.find_element(By.XPATH, "//a[@id='navNodeAnchor_1_2']").click()

# classfind = driver.find_elements(By.ID, 'Link6875f4d1')
# classfind = driver.find_element(By.ID, 'Link6875f4d1')
# classfind.click()
# print(classfind.__sizeof__())

driver.switch_to.frame("ivuFrm_page0ivu3")
driver.find_element(By.LINK_TEXT, 'Student Self Service').click()

# driver.find_element(By.XPATH, "//span[@id='TextView50aceda5']").click()


#driver.get(driver.current_url)

attendance = driver.find_element(By.LINK_TEXT, 'Student Attendance Details')

try:
    attendance.click()
except StaleElementReferenceException:
    attendance = driver.find_element(By.LINK_TEXT, 'Student Attendance Details')
    attendance.click()
# driver.find_element(By.ID,'TextView7685b3bc').click()

# bylink = driver.find_element(By.ID, 'Link2bda1807   ' )

# element = driver.execute_script('return document.getElementById("TextView290c36f6")')
# ele = driver.find_element
# driver.execute_script("arguments[0].click();",element)

# driver.execute_script("$('#TextView5db8705a-r').click()")

driver.switch_to.frame('isolatedWorkArea')
ele = driver.find_element(By.ID, 'WD52').click()
driver.find_element(By.ID, 'WD64').click()

driver.find_element(By.ID, 'WD6E').click()
driver.find_element(By.ID, 'WD71').click()
driver.find_element(By.ID, 'WD7B').click()

driver.maximize_window()

driver.execute_script("document.body.style.zoom = '125%'")


driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
time.sleep(2)

driver.save_screenshot("s1.png")

#driver.find_element(By.TAG_NAME, "body").send_keys(Keys.CONTROL, Keys.ADD)





#text = driver.find_element(By.ID, "contentAreaDiv").text
#print(text)
time.sleep(60)
driver.quit()