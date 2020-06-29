from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def check_popups(wd):
    print("check popups...")
    # "//div[text()='Select the language of your choice.']"
    # "//button[text()='English]"
    try: 
        wd.find_element_by_xpath("//div[text()='Select the language of your choice.']")
        print("Select language found!")
    except Exception as e:
        print(e)
        print("Select language NOT found!")

    try: 
        wd.find_element_by_xpath("//button[text()='English']").click()
        print("English found!")
    except Exception as e:
        print(e)
        print("English NOT found!")

    time.sleep(3)
    # div class="hf-language-menu-container" "//div[@class='hf-language-menu-container']"
    # <p class="nav-bold">United States</p> "//p[text()='United States']"
    try: 
        wd.find_element_by_xpath("//p[text()='United States']").click()
        print("US found!")
    except Exception as e:
        print(e)
        print("US NOT found!")

    time.sleep(5)

def check_if_user_is_logged(wd):
    # "//a[@id='MyAccountLink']"
    try: 
        wd.find_element_by_xpath("//a[@id='MyAccountLink']").click()
        print("MyAccountLink found!")
    except:
        print("MyAccountLink NOT found!")

#driver = webdriver.Chrome('chromedriver')
driver = webdriver.Firefox()
#driver.implicitly_wait(10)

driver.get("http://www.nike.com")
print(driver.title)

driver.implicitly_wait(20)
check_popups(driver)

# "//div[@id='AccountNavigationContainer']"
driver.find_element_by_xpath("//div[@id='AccountNavigationContainer']").click()
check_popups(driver)

# exit()

#driver.get("http://www.nike.com/login")

driver.find_element_by_xpath("//input[@name='emailAddress']").send_keys("g01uniecom@gmail.com")
driver.find_element_by_xpath("//input[@name='password']").send_keys("Bazinga!1")

#driver.find_element_by_xpath("//input[@type='button']").click()
driver.find_element_by_xpath("//input[@value='SIGN IN']").click()

time.sleep(5)
check_if_user_is_logged(driver)
driver.close()