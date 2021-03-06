from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginPages:
    textbox_username_id='input_email'
    textbox_password_id='input_password'
    button_login_id='submit_login'
    link_logout_linktext='Log out'
    classname_eye_password= 'MuiIconButton-label'
    forgot_linktext= 'btn_to-forgot-password'
    facebook_login= "login_facebook"

    def __init__(self,driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.ID, (self.textbox_username_id)).clear()
        self.driver.find_element(By.ID, (self.textbox_username_id)).click()
        self.driver.find_element(By.ID, (self.textbox_username_id)).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, (self.textbox_password_id)).clear()
        self.driver.find_element(By.ID, (self.textbox_password_id)).click()
        self.driver.find_element(By.ID, (self.textbox_password_id)).send_keys(password)

    def enterLogin(self):
        self.driver.find_element(By.ID, (self.textbox_password_id)).send_keys(Keys.ENTER)

    def eyePassword(self):
        self.driver.find_element(By.CLASS_NAME, (self.classname_eye_password)).click()

    def clickLogin(self):
        self.driver.find_element(By.ID, (self.button_login_id)).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, (self.link_logout_linktext)).click()

    def clickFBLogin(self):
        self.driver.find_element(By.ID, (self.facebook_login)).click()

    def TABkey(self):
        self.driver.find_element(By.ID, (self.textbox_username_id)).click()
        self.driver.find_element(By.ID, (self.textbox_username_id)).send_keys("percobaan")
        self.driver.find_element(By.ID, (self.textbox_username_id)).send_keys(Keys.TAB)
        self.driver.find_element(By.ID, (self.textbox_password_id)).send_keys("percobaan")
        self.driver.find_element(By.ID, (self.forgot_linktext)).send_keys(Keys.TAB)
        self.driver.find_element(By.ID, (self.button_login_id)).send_keys(Keys.TAB)