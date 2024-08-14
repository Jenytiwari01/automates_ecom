import random
import time
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException


# Set up Chrome options
# chrome_options = Options()
# chrome_options.add_argument("--start-maximized")

# Path to the chromedriver executable
chrome_driver_path = r'C:\drivers\chromedriver\chromedriver.exe'

# Initialize webdriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Open URL and maximize window
driver.get('http://tutorialsninja.com/demo/')
driver.maximize_window()

# Phones button
phones = driver.find_element(By.XPATH, '//a[text()="Phones & PDAs"]')
phones.click()

# iPhone
iphone = driver.find_element(By.XPATH, '//a[text()="iPhone"]')
iphone.click()
time.sleep(1)

# First picture
first_pic = driver.find_element(By.XPATH, '//ul[@class="thumbnails"]/li[1]')
first_pic.click()
time.sleep(2)

# Next picture
next_click = driver.find_element(By.XPATH, '//button[@title="Next (Right arrow key)"]')

for i in range(5):
    next_click.click()
    time.sleep(2)

# Save screenshot
# driver.save_screenshot(f'screenshot#{random.randint(0, 101)}.png')
# Save screenshot
screenshot_filename = 'screenshot#' + str(random.randint(0, 101)) + '.png'
driver.save_screenshot(screenshot_filename)
print(f"Screenshot saved as {screenshot_filename}")

# Close the browser

#close
x_button=driver.find_element(By.XPATH, '//button[@title="Close (Esc)"]')
x_button.click()
time.sleep(1)

#quantity
quantity=driver.find_element(By.ID, 'input-quantity')
quantity.click()
time.sleep(1)

quantity.clear()
time.sleep(1)
quantity.send_keys('2')
time.sleep(1)

#add to cart
add_to_button=driver.find_element(By.ID, 'button-cart')
add_to_button.click()
time.sleep(2)


laptops=driver.find_element(By.XPATH, '//a[text()="Laptops & Notebooks"]')
action=ActionChains(driver)
action.move_to_element(laptops).perform()
time.sleep(2)
laptops_2=driver.find_element(By.XPATH,'//a[text()="Show AllLaptops & Notebooks"]')
laptops_2.click()
time.sleep(1)

#click on HP laptop
HP=driver.find_element(By.XPATH,'//a[text()="HP LP3065"]')
HP.click()

#scroll
add_to_button_2=driver.find_element(By.XPATH,'//button[@id="button-cart"]')
add_to_button_2.location_once_scrolled_into_view
time.sleep(1)

calendar=driver.find_element(By.XPATH, '//i[@class="fa fa-calendar"]')
calendar.click()
time.sleep(1)

next_click_calendar=driver.find_element(By.XPATH,'//th[@class="next"]')
month_year=driver.find_element(By.XPATH,'//th[@class="picker-switch"]')

#year:2022 month:december
while month_year.text != 'December 2022':
    next_click_calendar.click()
time.sleep(2)

#day 31
calendar_date=driver.find_element(By.XPATH, '//td[text()="31"]')
calendar_date.click()
time.sleep(2)

#add to button
add_to_button_2.click()
time.sleep(1)

#Checkout
go_to_cart=driver.find_element(By.ID,'cart-total')
go_to_cart.click()
time.sleep(1)

checkout=driver.find_element(By.XPATH,'//p[@class="text-right"]/a[2]')
checkout.click()
time.sleep(1)

#click on guest account
try:
    # Add an explicit wait for the page to load completely if necessary
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//input[@value="guest"]')))

    guest = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, '//input[@value="guest"]'))
    )
    guest.click()
    print("Clicked on guest account.")
except TimeoutException:
    print("TimeoutException: Guest account element not found or not interactable.")
    driver.save_screenshot('timeout_guest_element.png')
    print("Screenshot saved as 'timeout_guest_element.png'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    driver.save_screenshot('unexpected_error.png')
    print("Screenshot saved as 'unexpected_error.png'.")

# Click continue 1
try:
    continue_1 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, 'button-account'))
    )
    continue_1.click()
    print("Clicked on Continue button.")
except TimeoutException:
    print("TimeoutException: Continue button element not found or not interactable.")
    driver.save_screenshot('timeout_continue_button.png')
    print("Screenshot saved as 'timeout_continue_button.png'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    driver.save_screenshot('unexpected_continue_error.png')
    print("Screenshot saved as 'unexpected_continue_error.png'.")


step_2=driver.find_element(By.XPATH,'//a[text()="Step 2: Billing Details "]')
step_2.location_once_scrolled_into_view
time.sleep(2)

#first name
first_name=driver.find_element_by_id('input-payment-firstname')
first_name.click()
time.sleep(1)
first_name.send_keys('test_first_name')
time.sleep(1)

#last_name
last_name=driver.find_element_by_id('input-payment-lastname')
last_name.click()
time.sleep(1)
last_name.send_keys('test_last_name')
time.sleep(1)

#email
email=driver.find_element_by_id('input-payment-email')
email.click()
time.sleep(1)
email.send_keys('test@test.com')
time.sleep(1)

#telephone
telephone=driver.find_element_by_id('input-payment-telephone')
telephone.click()
time.sleep(1)
telephone.send_keys('012345678')
time.sleep(1)

#address
address=driver.find_element_by_id('input-payment-address-1')
address.click()
time.sleep(1)
address.send_keys('teststreet 187')
time.sleep(1)

#city
city=driver.find_element_by_id('input-payment-city')
city.click()
time.sleep(1)
city.send_keys('Frankfurt')
time.sleep(1)

#postcode
postcode=driver.find_element_by_id('input-payment-postcode')
postcode.click()
time.sleep(1)
postcode.send_keys('112233')
time.sleep(1)


#country
country=driver.find_element_by_id('input-payment-country')
dropdown_1=Select(country)
time.sleep(1)
dropdown_1.select_by_index(87)
time.sleep(1)

#region
region=driver.find_element_by_id('input-payment-zone')
dropdown_2=Select(region)
time.sleep(1)
dropdown_2.select_by_visible_text('Hessen')
time.sleep(1)

#click continue 2
continue_2=driver.find_element_by_xpath('//input[@id="button-guest"]')
continue_2.click()
time.sleep(1)

#click continue 3
continue_3=driver.find_element_by_xpath('//input[@id="button-shipping-method"]')
continue_3.click()
time.sleep(1)

#accept terms & conditions
t_e=driver.find_element_by_xpath('//input[@name="agree"]')
t_e.click()
time.sleep(1)

#click continue 4
continue_4=driver.find_element_by_xpath('//input[@id="button-payment-method"]')
continue_4.click()
time.sleep(3)

#final price
final_price=driver.find_element_by_xpath('//table[@class="table table-bordered table-hover"]/tfoot/tr[3]/td[2]')

print("The final price of both products is " + final_price.text)
time.sleep(2)

#click on the confirmation button
confirmation_button=driver.find_element_by_id('button-confirm')
confirmation_button.click()
time.sleep(2)


#success text
success_text=driver.find_element_by_xpath('//div[@class="col-sm-12"]/h1')
print(success_text.text)
time.sleep(1)

driver.close()