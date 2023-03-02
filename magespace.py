from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
import pickle
import requests
import math
import os
class magebot:
    def __init__(self,path : str):
        if (not os.path.exists(os.getcwd()+"/magedata")):
            print("it looks like you don't have any user data dirs for chromium!")
            inp = input("enter your email for the mage space(p.s. you don't need to sign up there): ")
            print("starting browser...")
            options = Options()
            options.set_capability("goog:loggingPrefs", {"performance": "ALL", "browser": "ALL"})
            options.add_argument('--headless=new')
            options.add_argument('--disable-gpu')
            options.add_argument("user-data-dir="+os.getcwd()+"/magedata")
            options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36")
            self.driver = webdriver.Chrome(options=options,executable_path=path)
            self.driver.get("https://www.mage.space/")
            self.driver.refresh()
            time.sleep(1)
            self.driver.find_element(By.XPATH, "//button[@class='mantine-UnstyledButton-root mantine-Button-root mantine-1hhkg6n']").click()
            self.driver.find_element(By.XPATH, "//input[@class='mantine-o0oj3t mantine-Checkbox-input']").click()
            time.sleep(0.2)
    
            h = self.driver.find_element(By.XPATH, "//div[@class='mantine-Input-wrapper mantine-TextInput-wrapper mantine-12sbrde']/input")
            h.send_keys(inp)
            h.send_keys(Keys.ENTER)
            time.sleep(2)
            print("you should receive a link in your inbox")
            inp2 = input("enter it here: ")
            self.driver.get(inp2)
            time.sleep(5)
            print("you are now logged in to mage.space, congrats!")
        else:
            # create webdriver object
            self.options = Options()
            self.options.set_capability("goog:loggingPrefs", {"performance": "ALL", "browser": "ALL"})
            self.options.add_argument('--headless=new')
            self.options.add_argument('--disable-gpu')
            self.options.add_argument("user-data-dir="+os.getcwd()+"/magedata")
            self.options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36")
            self.driver = webdriver.Chrome(options=self.options,executable_path=path)
            self.driver.get("https://www.mage.space/")
            return 
    def ask(self,input_text : str,**args):
        self.driver.find_element(By.XPATH, "//button[@class='mantine-UnstyledButton-root mantine-Button-root mantine-1hhkg6n']").click()
        self.driver.find_element(By.XPATH, "//input[@class='mantine-o0oj3t mantine-Checkbox-input']").click()
        self.driver.find_element(By.XPATH, "//button[@class='mantine-UnstyledButton-root mantine-Button-root mantine-1qsvvs3']").click()
        time.sleep(0.1)
        #self.driver.find_element(By.XPATH, "//div[@class='mantine-8jlqcf mantine-Switch-trackLabel']").click()
        if args.get("model") == 'stable1.5':
            self.driver.find_element(By.XPATH, "//div[@class='mantine-Group-root mantine-5f6x53']/div[1]/button[1]").click()
        elif args.get("model") == "stable2.5":
            self.driver.find_element(By.XPATH, "//div[@class='mantine-Group-root mantine-5f6x53']/div[1]/button[2]").click()
        if args.get("ratio") =="16:9":
            g = self.driver.find_elements(By.XPATH, "//div[@class='mantine-Group-root mantine-5f6x53']")[4]
            g.find_elements(By.XPATH,"button")[0].click()
        elif args.get("ratio") =="3:2":
            g = self.driver.find_elements(By.XPATH, "//div[@class='mantine-Group-root mantine-5f6x53']")[4]
            g.find_elements(By.XPATH,"button")[1].click()
        elif args.get("ratio") =="1:1":
            g = self.driver.find_elements(By.XPATH, "//div[@class='mantine-Group-root mantine-5f6x53']")[4]
            g.find_elements(By.XPATH,"button")[2].click()
        elif args.get("ratio") =="2:3":
            g = self.driver.find_elements(By.XPATH, "//div[@class='mantine-Group-root mantine-5f6x53']")[4]
            g.find_elements(By.XPATH,"button")[3].click()
        elif args.get("ratio") =="9:16":
            g = self.driver.find_elements(By.XPATH, "//div[@class='mantine-Group-root mantine-5f6x53']")[4]
            g.find_elements(By.XPATH,"button")[4].click()
        if args.get("steps") != None:
            steps = self.driver.find_element(By.XPATH, "//div[@class='mantine-9qjq5y mantine-Slider-track'][1]/div[2]")
            for i in range(int(steps.get_attribute("aria-valuenow"))-10):
                steps.send_keys(Keys.LEFT)
            if args.get("steps") >=10 and args.get("steps") <= 150:
                for i in range(args.get("steps")-10):
                    steps.send_keys(Keys.RIGHT)
        if args.get("scale") != None:
            sca = self.driver.find_elements(By.XPATH, "//div[@class='mantine-9qjq5y mantine-Slider-track']")[1]
            scale = sca.find_element(By.XPATH, ".//div[2]")
            for i in range(int(float(scale.get_attribute("aria-valuenow"))*10)):
                scale.send_keys(Keys.LEFT)
            if args.get("scale") <= 30:
                for i in range(int(float(args.get("scale")*10))):
                    scale.send_keys(Keys.RIGHT)
        
        if args.get("seed") != None:
            elem = self.driver.find_element(By.XPATH, "//input[@class='mantine-Input-input mantine-NumberInput-input mantine-1eb2xr4']")
            elem.send_keys(args.get("seed"))
        if args.get("negprompt") != None:
            elem = self.driver.find_element(By.XPATH, "//input[@class='mantine-Input-input mantine-Textarea-input mantine-67te2a']")
            elem.send_keys(args.get("negprompt"))
        element = self.driver.find_element(By.ID, "search-bar")
        element.send_keys(input_text)
        element.send_keys(Keys.ENTER)
        imlist =[]
        while True:
            list = []
            log_entries = self.driver.get_log("performance")
            for entry in log_entries:
                obj_serialized: str = entry.get("message")
                obj = json.loads(obj_serialized)
                message = obj.get("message").get("params").get("type")
                list.append(message)
            if ("Image" in list):
                imlist.append("img")
            if len(imlist) >= 3:
                break
            time.sleep(0.5)
        elementer = self.driver.find_elements(By.XPATH,"//img[@class='mantine-gvt5r2 mantine-Image-image']")
        return elementer[-1].get_attribute("src")

#print(magebot("/home/dood/.cache/selenium/chromedriver/linux64/110.0.5481.77/chromedriver"))