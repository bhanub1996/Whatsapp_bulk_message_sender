from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Provide the path to your Chrome webdriver
driver = webdriver.Chrome()
options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
# to supress the error messages/logs
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# Open WhatsApp web
driver.get('https://web.whatsapp.com/')
# print(webdriver_driver)
time.sleep(30)
# wait = WebDriverWait(driver, 60)
contact_numbers = ['+919490913503', '+919492126187']  # Add your contact numbers here

# Message to be sent
message = "Hello, this is a test message."

# for number in contact_numbers:
#     try:
#         url = 'https://web.whatsapp.com/send?phone={}&text={}'.format(number, message)
#         sent = False
#         # It tries 3 times to send a message in case if there any error occurred
#         driver.get(url)
#         try:
#             click_btn = WebDriverWait(driver, 35).until(
#                 EC.element_to_be_clickable((By.CLASS_NAME, '_3XKXx')))
#         except Exception as e:
#             print("Sorry message could not sent to " + str(number))
#         else:
#             time.sleep(2)
#             click_btn.click()
#             sent = True
#             time.sleep(5)
#             print('Message sent to: ' + str(number))
#         count = count + 1
#     except Exception as e:
#         print('Failed to send message to ' + str(number + str(e)))

# Loop through each contact number and send the message
for number in contact_numbers:
    try:
        # Find the search bar and search for the contact number
        search_bar = driver.find_element("xpath", '//div[@contenteditable="true"]')
        search_bar.clear()
        search_bar.send_keys(number)
        search_bar.send_keys(Keys.ENTER)
        time.sleep(2)  # Wait for the chat to load

        # Find the message input box and send the message
        # message_box = driver.find_element("xpath", '//div[@contenteditable="true"][@data-tab="1"]')
        # xpath_send_button = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]'
        #xpath_message_box = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div'
        # message_box = WebDriverWait(driver, 35).until(
        #         EC.element_to_be_selected((By.CLASS_NAME,''))
        #         element_to_be_clickable((By.CLASS_NAME, '_3XKXx')))
        # message_box = WebDriverWait(driver, 35).until(
        #         EC.element_to_be_clickable((By.CLASS_NAME, '_3XKXx')))

        message_box = driver.find_element("xpath", '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div')
        time.sleep(2)
        message_box.clear()
        message_box.send_keys(message)
        message_box.send_keys(Keys.ENTER)
        time.sleep(2)  # Wait before sending the next message

        print(f"Message sent to {number}")

    except Exception as e:
        print(f"Error sending message to {number}: {str(e)}")

# Close the browser
# driver.quit()