from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os

load_dotenv()

#USERNAME = os.getenv("USERNAME")
USERNAME = "jelp.m"
PASSWORD = os.getenv("PASSWORD")
MAX_TIME_LOAD = 20
MIN_TIME_LOAD = 2

xpath = {
   "decline_cookies": "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]",
    "save_login_not_now_button": "//div[contains(text(), 'Ahora no')]",
    "notification_not_now_button": "//button[contains(text(), 'Ahora no')]",
    "like_button": "//*[@aria-label='Me gusta']",
    "modal": "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]",
    "cancel_unfollow_button": "//button[contains(text(), 'Cancel')]",
}

css_selector = {
    "follows_buttons": "._aano button"
}

urls = {
    "login": "https://www.instagram.com/accounts/login/",
    "post": "https://www.instagram.com/p/CzZQt6BIsck/"
}


class InstaFollower:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get(urls["login"])

        try:
            cookie_warning = WebDriverWait(self.driver, MIN_TIME_LOAD).until(
                EC.presence_of_element_located((By.XPATH, xpath["decline_cookies"]))
            )
            # Dismiss the cookie warning by clicking an element or button
            cookie_warning[0].click()
        except:
            pass

        username = self.driver.find_element(by=By.NAME, value="username")
        password = self.driver.find_element(by=By.NAME, value="password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        WebDriverWait(self.driver, MIN_TIME_LOAD)
        password.send_keys(Keys.ENTER)

        try:
            # Click "Not now" and ignore Save-login info prompt
            save_login_prompt = WebDriverWait(self.driver, MIN_TIME_LOAD).until(
                EC.presence_of_element_located((By.XPATH, xpath["save_login_not_now_button"]))
            )
            save_login_prompt.click()
        except:
            pass

        try:
            # Click "not now" on notifications prompt
            notifications_prompt = WebDriverWait(self.driver, MIN_TIME_LOAD).until(
                EC.presence_of_element_located((By.XPATH, xpath["notification_not_now_button"]))
            )
            notifications_prompt.click()
        except:
            pass

    def like_to_post(self):
        self.driver.get(xpath["post"])

        # Click like
        like_button = WebDriverWait(self.driver, MAX_TIME_LOAD).until(
        EC.element_to_be_clickable((By.XPATH, xpath["like_button"]))
        )
        like_button.click()
        print("Like dado")
    
    def find_followers(self, account_name):
        WebDriverWait(self.driver, MIN_TIME_LOAD)

        # Show followers of the selected account. 
        self.driver.get(f"https://www.instagram.com/{account_name}/followers/")

        # The xpath of the modal that shows the followers will change over time. Update yours accordingly.
        modal = WebDriverWait(self.driver, MAX_TIME_LOAD).until(
            EC.presence_of_element_located((By.XPATH, xpath["modal"]))
        )
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            WebDriverWait(self.driver, MIN_TIME_LOAD)
  

    def follow(self):
        # Check and update the (CSS) Selector for the "Follow" buttons as required. 
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value=css_selector["follows_buttons"])

        for button in all_buttons:
            try:
                button.click()
                WebDriverWait(self.driver, MIN_TIME_LOAD)

            # Clicking button for someone who is already being followed will trigger dialog to Unfollow/Cancel
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value=xpath["cancel_unfollow_button"])
                cancel_button.click()     

bot = InstaFollower()
bot.login()
bot.find_followers("librofertas_")
