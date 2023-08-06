from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import string
import random

options = webdriver.ChromeOptions() 
options.add_experimental_option('detach',True)
options.add_argument('window-size=1400x900')

driver = webdriver.Chrome(options=options)
driver.get('https://accounts.google.com/signup/v2/createusername?flowName=GlifWebSignIn&flowEntry=SignUp&TL=AJvNCbZXXTdr26qzPcw0ou0CmN6OPGPQ7agM7pVjHwnQ3mm5lXcIfhAT84O1Yymc')

#Name
firstName = driver.find_element('name','firstName')
firstName.send_keys('Nico')
lastName = driver.find_element('name','lastName')
lastName.click()
lastName.send_keys('Robin')
nextButton = driver.find_element(By.CLASS_NAME, 'VfPpkd-dgl2Hf-ppHlrf-sM5MNb')
nextButton.click()

#DOB & Gender
try: # making sure the element exists before we click on it 
    month = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//select[@id='month']"))
    )
    month.click()
except:
    driver.quit()
    
select_month = Select(driver.find_element(By.ID, 'month'))
select_month.select_by_value('1')

day = driver.find_element('name', 'day')
day.click()
day.send_keys('1')

year = driver.find_element('name', 'year')
year.click()
year.send_keys('2001')

gender = driver.find_element(By.CLASS_NAME, 'ZyruUe')
gender.click()
select_gender = Select(driver.find_element(By.ID, 'gender'))
select_gender.select_by_value('1')

nextButton1 = driver.find_element(By.ID, 'birthdaygenderNext')
nextButton1.click()

# Choose your Gmail address
username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
print('Username: ' + username)

def gmail_username():
    try: 
        create_gmail1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='Username']")))
        create_gmail1.send_keys(username)
        NextButton0 = driver.find_element(By.CLASS_NAME, 'VfPpkd-dgl2Hf-ppHlrf-sM5MNb')
        NextButton0.click()
    except: 
        return False

case1 = gmail_username()

if case1 == False:
    create_gmail = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='selectionc2']")))
    print(str(create_gmail.is_displayed()))
    create_gmail.click()
    username_input = driver.find_element(By.XPATH,"//input[@name='Username']")
    username_input.send_keys(username)
    nextButton2 = driver.find_element(By.XPATH, "//span[normalize-space()='Next']")
    nextButton2.click()

#create password
password = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
print('Password: ' + password)
password_input = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='Passwd']")))
password_input.send_keys(password)
confirm_password = driver.find_element(By.XPATH, "//input[@name='PasswdAgain']")
confirm_password.click()
confirm_password.send_keys(password)

nextButton3 = driver.find_element(By.XPATH, "//span[@class='VfPpkd-vQzf8d']")
nextButton3.click() 

#In the event you are required to add a recovery email
try: 
    skip = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-INsAgc VfPpkd-LgbsSe-OWXEXe-dgl2Hf Rj2Mlf OLiIxf PDpWxe P62QJc LQeN7 xYnMae TrZEUc lw1w4b VfPpkd-ksKsZd-mWPk3d-OWXEXe-AHe6Kc-XpnDCe']//div[@class='VfPpkd-RLmnJb']")
            ))
    skip.click()
except: 
    pass

#Verify with phone number
add_phone_number = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, "//input[@id='phoneNumberId']")))
add_phone_number.send_keys('4055495732')
nextButton4 = driver.find_element(By.CLASS_NAME, 'VfPpkd-dgl2Hf-ppHlrf-sM5MNb')
nextButton4.click()

verification_code = input('Enter code: G-')
verify = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='code']")))
verify.click()
verify.send_keys(verification_code)
nextButton5 = driver.find_element(By.CLASS_NAME, 'VfPpkd-dgl2Hf-ppHlrf-sM5MNb')
nextButton5.click()

#skip add recovery email 
skip = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.CLASS_NAME, 'VfPpkd-vQzf8d')))
skip.click()

#In the event you are required to add your phone number again 
action = ActionChains(driver)
try: 
    phoneNumber =  WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.XPATH, "//input[@id='phoneNumberid']"))
    action.double_click(phoneNumber)
    phoneNumber.send_keys('delete')
    skip1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.XPATH, "//span[normalize-space()='Skip']"))
except: 
    pass 
    



    
    




