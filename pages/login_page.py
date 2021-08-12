from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC


class LoginPage():

    #Locater 
    EMAIL_FIELD = (By.NAME, "email")
    NEXT_BUTTON = (By.CSS_SELECTOR, ".mdl-button--colored")
    PASSWORD_FIELD = (By.NAME, "password")
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, ".mdl-button--colored") 


    def __init__(self,  browser:webdriver.Remote):
        self.driver = browser

    def load(self):
        self.driver.get("https://staging-partner-explore.misterb2b.com/login")
    
    #Method 
    def set_email_field(self, email):
        input_email_field = self.driver.find_element(*self.EMAIL_FIELD)
        input_email_field.send_keys(email)
    
    def click_next_button(self):
        next_button = self.driver.find_element(*self.NEXT_BUTTON)
        next_button.click()

    def set_password_field(self, password):
        input_password_field = self.driver.find_element(*self.PASSWORD_FIELD)
        input_password_field.send_keys(password)

    def click_sign_in_button(self):
        sign_in_button = self.driver.find_element(*self.SIGN_IN_BUTTON)
        sign_in_button.click()



        
    

