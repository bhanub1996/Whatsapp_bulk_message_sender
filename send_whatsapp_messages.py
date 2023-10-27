# import time
# import pandas as pd
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# def send_whatsapp_message(phone, message, image_path):
#     try:
#         driver.get(f'https://web.whatsapp.com/send?phone={phone}')
#         wait = WebDriverWait(driver, 60)

#         # Wait for the input box to load
#         input_box = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')))
#         input_box.send_keys(message)
#         time.sleep(1)

#         # Attach image
#         clip_button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div')
#         clip_button.click()

#         image_box = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/span/div/div/ul/li[1]/button/input')))
#         image_box.send_keys(image_path)

#         # Wait for image to upload and then send
#         send_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[1]/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div')))
#         send_button.click()
#     except Exception as e:
#         print(f"Error when sending to {phone}. Maybe the number is not registered on WhatsApp or other issues. Error: {e}")

# if __name__ == "__main__":
#     # Initialize the browser and open WhatsApp Web
#     driver = webdriver.Chrome() #executable_path='path_to_chromedriver')  # Change path_to_chromedriver to your chromedriver path
#     driver.get('https://web.whatsapp.com/')

#     # Wait for user to scan the QR Code
#     input("Press Enter after scanning the QR code..")

#     # Read the CSV file
#     df = pd.read_csv("C:/Users/bhanu/Downloads/BULK MESSAGES.csv")  # assuming you have a column 'phone' and 'message' in the CSV

#     # Image path that's common for all contacts
#     image_path = 'jpg_path'  # Replace with your actual path

#     message = """Friends🙏 

# Elevate your financial journey! 😆🚀🌟
# With
#    🎉💰 Money & Spirituality: A Gateway to Prosperity & Success
# A 2-day Workshop
# From QLU (Quantum Life University)
# At
# Life Foundation, Banjara Hills, Hyderabad. 


# Click here 👇 to avail  details now
# https://rzp.io/l/ZhDsHKCmZ 
# """

#     for index, row in df.iterrows():
#         message = "Namaste "+row['name']+message
#         send_whatsapp_message(row['phone'], message, image_path)
#         if index == 0:
#             break

#     driver.close()



import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def send_whatsapp_message(phone, message, image_path = 'C:/Users/bhanu/Downloads/MS.jpg'):
    # URL for sending message
    input_box = None
    try:
        driver.get(f'https://web.whatsapp.com/send?phone={phone}')
        wait = WebDriverWait(driver, 60)

        # Wait for the input box to load
        input_box = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')))
        input_box.send_keys(message)
        time.sleep(1)

        # Attach image
        clip_button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div')
        clip_button.click()

        image_box = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/span/div/div/ul/li[1]/button/input')))
        image_box.send_keys(image_path)

        # Wait for image to upload and then send
        send_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[1]/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div')))
        send_button.click()
    except Exception as e:
        print(f"Error when sending to {phone}. Maybe the number is not registered on WhatsApp. Error: {e}")
        return

    if input_box:
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)

if __name__ == "__main__":
    # Initialize the browser and open WhatsApp Web
    driver = webdriver.Chrome()#executable_path="C:/chrome-win64/chrome.exe")  # Change path_to_chromedriver to your chromedriver path
    # driver.get('https://web.whatsapp.com/')

    # # Wait for user to scan the QR Code
    input("Press Enter after scanning the QR code..")

    # Read the CSV file
    df = pd.read_csv("C:/Users/bhanu/Downloads/BULK MESSAGES.csv")  # assuming you have columns 'phone' and 'message' in the CSV

    message = """🙏 

            Elevate your financial journey! 😆🚀🌟
            With
            🎉💰 Money & Spirituality: A Gateway to Prosperity & Success
            A 2-day Workshop
            From QLU (Quantum Life University)
            At
            Life Foundation, Banjara Hills, Hyderabad. 


            Click here 👇 to avail  details now
            https://rzp.io/l/ZhDsHKCmZ 
            """         

    for index, row in df.iterrows():
        print(row['phone'])
        print(row['name'])
        message = "Namaste "+row['name']+message
        
        send_whatsapp_message(row['phone'], message)
        print("sent")
        if index == 1:
            break
        

    driver.close()