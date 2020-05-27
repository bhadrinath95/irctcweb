from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait,Select
import time 

import datetime
import os
from xxsubtype import bench

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def irctc(req, Person):
    status = ''
    try:
        driver = webdriver.Chrome(executable_path=os.path.join(BASE_DIR, "lib\chromedriver.exe"))  
        driver.get('https://www.irctc.co.in/')
        driver.maximize_window()
        driver.refresh()
        driver.implicitly_wait(100)
        driver.find_element_by_xpath("//button[text()='Ok']").click()
        driver.implicitly_wait(100)
        driver.find_element_by_xpath("//a[text()=' LOGIN ']").click()
        driver.implicitly_wait(100)
        driver.find_element_by_xpath("//input[@name='userId']").send_keys(req.irctc_username)
        driver.implicitly_wait(100)
        driver.find_element_by_xpath("//input[@name='pwd']").send_keys(req.irctc_password)
        driver.implicitly_wait(100)
        driver.find_element_by_xpath("//input[@name='otpLogin']").click()
        driver.implicitly_wait(100)
        driver.find_element_by_xpath("//button[text()='SIGN IN']").click()
        driver.implicitly_wait(100)
        l = 0
        print("Started Waiting")
        while True:
            l = l +1
            try:
                driver.find_element_by_xpath("//button[text()='Ok']").click()
                driver.find_element_by_xpath("//button[@label='Find Trains']").click()
                break
            except:
                pass
            if l > 100:
                break
                
        print("Waiting is over")
        driver.find_element_by_xpath("//input[@placeholder='Journey Date(dd-mm-yyyy)*']").send_keys(Keys.CONTROL, 'a')
        driver.find_element_by_xpath("//input[@placeholder='Journey Date(dd-mm-yyyy)*']").send_keys(Keys.BACKSPACE)
        driver.implicitly_wait(100)
        driver.find_element_by_xpath("//input[@placeholder='Journey Date(dd-mm-yyyy)*']").send_keys(datetime.datetime.strptime(str(req.travel_date), '%Y-%m-%d').strftime('%d-%m-%Y'))
        driver.implicitly_wait(100) 
        driver.find_element_by_xpath("//button[@label='Find Trains']").click()
        driver.implicitly_wait(100)
        driver.find_element_by_xpath("//*[@id='journeyClass']/div/label").click()
        driver.implicitly_wait(100)
        driver.find_element_by_xpath(f"""//span[text()='{req.travel_class}']""").click()
        driver.implicitly_wait(100)
        driver.find_element_by_xpath("//button[@label='Find Trains']").click()
        driver.implicitly_wait(100)
        driver.find_element_by_xpath("//*[@id='origin']/span/input").send_keys(req.source)
        driver.implicitly_wait(100)
        driver.find_element_by_xpath("//*[@id='destination']/span/input").send_keys(req.destination)
        driver.implicitly_wait(100)
        driver.find_element_by_xpath("//*[@id='origin']/span/input").click()
        driver.implicitly_wait(100)
        driver.find_element_by_xpath("//button[@label='Find Trains']").click()
        driver.implicitly_wait(100)
        print(f"""//a[@id='T_{req.train_number}']//parent::div//parent::div//parent::div//parent::div//button""")
        #driver.find_element_by_xpath(f"""//a[@id='T_{req.train_number}']//parent::div//parent::div//parent::div//parent::div//button""").click()
        try:
            driver.find_element_by_xpath(f"""//a[@id='T_{req.train_number}']//parent::div//parent::div//parent::div//parent::div//button""").click()
        except:
            driver.implicitly_wait(100)
            try:
                driver.find_element_by_xpath(f"""//a[@id='T_{req.train_number}']//parent::div//parent::div//parent::div//parent::div//button""").click()
            except:
                print("No such train exist")
        driver.implicitly_wait(10000)
        try:
            driver.find_element_by_xpath(f"""//span[text()='{datetime.datetime.strptime(str(req.travel_date), '%Y-%m-%d').strftime('%d %b %Y')}']//parent::div//parent::div//button""").click()
        except:
            print("No booking available for that date")
        driver.implicitly_wait(100)
        driver.find_element_by_xpath("//span[text()='I Agree']").click()
        driver.implicitly_wait(100)
        driver.find_element_by_xpath("//span[text()='Ok']").click()
        driver.implicitly_wait(100)
        
        count = 0
        for item in Person:
            if count != 0:
                driver.find_element_by_xpath("//span[text()='+ Add Passenger']").click()
                driver.implicitly_wait(100)
            count = count + 1
            driver.implicitly_wait(10000)
            driver.find_element_by_xpath(f"""//span[text()=' {count}']//parent::div//parent::div//input[@id='psgn-name']""").send_keys(item.person_name)
            driver.implicitly_wait(100)
            driver.find_element_by_xpath(f"""//span[text()=' {count}']//parent::div//parent::div//input[@formcontrolname='passengerAge']""").send_keys(item.person_age)
            driver.implicitly_wait(100)
            select = Select(driver.find_element_by_xpath(f"""//span[text()=' {count}']//parent::div//parent::div//select[@formcontrolname='passengerGender']"""))
            select.select_by_visible_text(item.gender)
            driver.implicitly_wait(100)
            select = Select(driver.find_element_by_xpath(f"""//span[text()=' {count}']//parent::div//parent::div//select[@formcontrolname='passengerBerthChoice']"""))
            select.select_by_visible_text(item.preference)
            driver.implicitly_wait(100)
            select = Select(driver.find_element_by_xpath(f"""//span[text()=' {count}']//parent::div//parent::div//select[@formcontrolname='passengerNationality']"""))
            select.select_by_value(item.nationality)
            driver.implicitly_wait(100)
            
        driver.find_element_by_xpath("//input[@id='address-flat']").send_keys(req.destination_address)
        driver.implicitly_wait(100)
        driver.find_element_by_xpath("//input[@id='address-street']").send_keys(req.destination_address_2)
        driver.implicitly_wait(100)
        driver.find_element_by_xpath("//input[@id='address-area']").send_keys(req.destination_address_3)
        driver.implicitly_wait(100)
        driver.find_element_by_xpath("//input[@id='address-PIN']").send_keys(req.destination_pin)
        driver.find_element_by_xpath("//input[@id='address-PIN']").send_keys(Keys.ENTER)
        driver.implicitly_wait(100)
        driver.find_element_by_xpath("//button[text()='Continue ']").click()
        driver.implicitly_wait(100)
        try:
            driver.find_element_by_xpath("//button[text()='Continue ']").click()
        except:
            pass
        driver.implicitly_wait(100)
        status = driver.find_element_by_xpath("//app-availability-summary/div/span[2]").text
        print(status)
        print("Wait started")
        while True:
            try:
                driver.implicitly_wait(2)
                driver.find_element_by_xpath("//label[text()='OTP for Booking ']").click()
                try:
                    driver.find_element_by_xpath("//p-confirmdialog/div/div[3]/p-footer/div/button[2]").click()
                except:
                    pass
                print('Checking')
                continue
            except:
                try:
                    driver.find_element_by_xpath("//p-confirmdialog/div/div[3]/p-footer/div/button[2]").click()
                except:
                    pass
                break
        print("Wait is over")
        driver.implicitly_wait(10000)
        driver.find_element_by_xpath(f"""//span[@class='ui-tabview-title' and text()='{req.payoption}']""").click()
        driver.implicitly_wait(10000)
        print(f"""//span[text()='{req.paymethod}']""")
        driver.find_element_by_xpath(f"""//span[text()='{req.paymethod}']""").click()
        driver.implicitly_wait(100)
        driver.find_element_by_xpath(f"""//span[text()='{req.paymethod}']//parent::label//parent::div//button[text()='Make Payment']""").click()
        try:
            print("Wait started2")
            
            waitForMinute = 3
            waitmin = 0
            
            while waitmin <= waitForMinute:
                i = 0
                while i < 12:
                    time.sleep(5)
                    print(driver.current_url)
                    i = i+1
                waitmin = waitmin + 1
                
            print("Wait is over")
            driver.close()
        except:
            pass
    except:
        pass
    
    try:
        driver.close()
    except:
        pass
    
    return status
            
        
    
#irctc()