from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
import time
from dotenv import load_dotenv
import os

load_dotenv()

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

class InstaFollower:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        url = "https://www.instagram.com/accounts/login/"
        self.driver.get(url)
        time.sleep(4)

        # Check if the cookie warning is present on the page
        decline_cookies_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]"
        cookie_warning = self.driver.find_elements(By.XPATH, decline_cookies_xpath)
        if cookie_warning:
            # Dismiss the cookie warning by clicking an element or button
            cookie_warning[0].click()

        username = self.driver.find_element(by=By.NAME, value="username")
        password = self.driver.find_element(by=By.NAME, value="password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        time.sleep(2)
        password.send_keys(Keys.ENTER)

        time.sleep(4)
        # Click "Not now" and ignore Save-login info prompt
        save_login_prompt = self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Ahora no')]")
        if save_login_prompt:
            save_login_prompt.click()

        time.sleep(3)
        # Click "not now" on notifications prompt
        notifications_prompt = self.driver.find_element(by=By.XPATH, value="// button[contains(text(), 'Ahora no')]")
        if notifications_prompt:
            notifications_prompt.click()
        
    def like_to_post(self):
        url = "https://www.instagram.com/p/CzZQt6BIsck/"
        self.driver.get(url)
        time.sleep(4)

        # Click like
        try:
            like_button = self.driver.find_element(by=By.XPATH, value="//*[@aria-label='Me gusta']")
            if like_button:
                like_button.click()
                print("Like dado")
        except Exception as e:
            print("No fue posible dar like. ",e)   
    
    def find_followers(self):
        SIMILAR_ACCOUNT = "tonydevpy"
        time.sleep(5)
        # Show followers of the selected account. 
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers/")

        time.sleep(5)
        # The xpath of the modal that shows the followers will change over time. Update yours accordingly.
        modal_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]"
        modal = self.driver.find_element(by=By.XPATH, value=modal_xpath)
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)  

    def follow(self):
        # Check and update the (CSS) Selector for the "Follow" buttons as required. 
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value='._aano button')

        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            # Clicking button for someone who is already being followed will trigger dialog to Unfollow/Cancel
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()    

    def find_followers(self):
        SIMILAR_ACCOUNT = "tonydevpy"
        time.sleep(5)
        # Show followers of the selected account. 
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")

        time.sleep(5)
        # The xpath of the modal that shows the followers will change over time. Update yours accordingly.
        modal_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]"
        modal = self.driver.find_element(by=By.XPATH, value=modal_xpath)

        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
        time.sleep(2)     

    def follow(self):
        # Check and update the (CSS) Selector for the "Follow" buttons as required. 
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value='._aano button')

        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            # Clicking button for someone who is already being followed will trigger dialog to Unfollow/Cancel
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()   

bot = InstaFollower()
bot.login()
