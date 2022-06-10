from selenium import webdriver
from utilities.dataLog import Log_Data
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
import time

#==================================================================
#       FIXTURE
#==================================================================
@pytest.fixture()
def driver():
        driver = webdriver.Chrome()
        driver.get('https://www.populix.co/login')
        driver.implicitly_wait(10)
        driver.set_window_size(697, 720)
        yield driver
        driver.quit()

log = Log_Data.custom_logger()

#==================================================================================================================
#   TESTCASE 1 : Verify user navigates to the proper page when selecting the forgot password link
#==================================================================================================================        

def test_1_function_forgot_password(driver):
        log.info("=== Test_1_FUNCTION forgot_password ===")
        driver.find_element(By.ID, "input_email").send_keys("tito@gmail.com")
        driver.find_element(By.ID, "btn_to-forgot-password").click()
        time.sleep(2)

        get_url = driver.current_url
        if get_url == 'https://www.populix.co/forgot-password':
            if 'Lupa kata sandi?' in driver.find_element(By.CLASS_NAME, 'MuiTypography-h4').text:
                assert True
                log.info("=== Test_1_FUNCTION forgot_password: PASS")
        else:
            log.error("=== Test_1_FUNCTION forgot_password: FAIL")
            driver.save_screenshot(".\\Screenshots\\" + "Test_1_FUNCTION forgot_password.png")
            assert False


#===================================================================================================================
#   TESTCASE 2 : Verify user navigates to the Facebook Login page when selecting LOGIN via facebook button
#==================================================================================================================        

def test_2_function_facebook(driver):
        log.info("=== Test_2_FUNCTION_facebook ===")
        driver.find_element(By.ID, "login_facebook").click()
        time.sleep(2)

        if 'https://www.facebook.com/login' in driver.current_url :
            if 'Facebook' in driver.find_element(By.CLASS_NAME, 'fb_logo').text:
                assert True
                log.info("=== Test_2_FUNCTION_facebook: PASS")
        else:
            log.error("=== Test_2_FUNCTION_facebook: FAIL")
            driver.save_screenshot(".\\Screenshots\\" + "Test_2_FUNCTION_facebook.png")
            assert False


#==================================================================================================================
#   TESTCASE 3 : Verify user navigates to the Google account page when selecting LOGIN via Google button
#==================================================================================================================        

def test_3_function_gmail(driver):
        log.info("=== Test_3_FUNCTION_gmail ===")
        driver.find_element(By.ID, "login_google").click()
        time.sleep(2)

        if 'https://accounts.google.com/' in driver.current_url :
            if 'Login dengan Google' in driver.find_element(By.CLASS_NAME, 'kHn9Lb').text:
                assert True
                log.info("=== Test_3_FUNCTION_gmail: PASS")
        else:
            log.error("=== Test_3_FUNCTION_gmail: FAIL")
            driver.save_screenshot(".\\Screenshots\\" + "Test_3_FUNCTION_gmail.png")
            assert False

#==================================================================================================================
#   TESTCASE 4 : Verify user navigates to the Register page when selecting Register/Daftar link text
#==================================================================================================================        

def test_4_function_register_button(driver):
        log.info("=== Test_4_FUNCTION_register_page ===")
        driver.find_element(By.ID, "btn_to-register").click()
        time.sleep(2)
        
        get_url = driver.current_url 
        if get_url == 'https://www.populix.co/register':
            if  'Daftar Akun Populix' in driver.find_element(By.CLASS_NAME, 'MuiTypography-h4').text :
                assert True
                log.info("=== Test_4_FUNCTION_register_page: PASS")
        else:
            log.error("=== Test_4_FUNCTION_register_page: FAIL")
            driver.save_screenshot(".\\Screenshots\\" + "Test_4_FUNCTION_register_page.png")
            assert False

#==================================================================================================================
#   TESTCASE 5 : Verify user navigates to the Google Play Store page when selecting Play Store Button
#==================================================================================================================        

def test_5_function_playstore_button(driver):
        log.info("=== Test_5_FUNCTION_playstore_page ===")
        driver.find_element(By.ID, "btn_to-playstore").click()
        time.sleep(2)
        
        get_url = driver.current_url
        if get_url == 'https://play.google.com/store/apps/details?id=co.populix' :
            if  'Google Play' in driver.find_element(By.CLASS_NAME, 'GMGZAc').text :
                assert True
                log.info("=== Test_5_FUNCTION_playstore_page: PASS")
        else:
            log.error("=== Test_5_FUNCTION_playstore_page: FAIL")
            driver.save_screenshot(".\\Screenshots\\" + "Test_5_FUNCTION_playstore_page.png")
            assert False

#==================================================================================================================
#   TESTCASE 6 : Verify user navigates to the Apple App Store page when selecting App Store Button
#==================================================================================================================        

def test_6_function_appstore_button(driver):
        log.info("=== Test_6_FUNCTION_appstore_page ===")
        driver.find_element(By.ID, "btn_to-appstore").click()
        time.sleep(2)

        get_url = driver.current_url
        if get_url == 'https://apps.apple.com/id/app/populix/id1509148327?l=id':
            if 'App Store' in driver.find_element(By.CLASS_NAME, 'we-localnav').text :        
                assert True
                log.info("=== Test_6_FUNCTION_appstore_page: PASS")
        else:
                log.error("=== Test_6_FUNCTION_appstore_page: FAIL")
                driver.save_screenshot(".\\Screenshot\\" + "Test_6_FUNCTION_appstore_page.png")
                assert False

#==================================================================================================================
#   TESTCASE 7 : Verify user navigates to the POPULIX HOME page when selecting POPULIX Logo in Login Page
#==================================================================================================================

def test_7_function_populixLogo_button(driver):
        log.info("=== Test_7_FUNCTION_populixLogo_button ===")
        driver.find_element(By.CSS_SELECTOR, '#root > div > div > div > div.jss7 > div > div > div > div.MuiCardContent-root.jss13 > a > img').click()
        time.sleep(2)

        get_url = driver.current_url
        if get_url == 'https://info.populix.co/':
            if 'Mengutamakan Kualitas Responden' in driver.find_element(By.CLASS_NAME, 'title').text :        
                assert True
                log.info("=== Test_7_FUNCTION_populixLogo_button: PASS")
        else:
                log.error("=== Test_7_FUNCTION_populixLogo_button: FAIL")
                driver.save_screenshot(".\\Screenshot\\" + "Test_7_FUNCTION_populixLogo_button.png")
                assert False