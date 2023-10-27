import time
import webbrowser as web
from datetime import datetime
from typing import Optional
from urllib.parse import quote
import pandas as pd

import pyautogui as pg

from pywhatkit.core import core, exceptions, log

import re

pg.FAILSAFE = False

core.check_connection()

def verify_indian_phone_number(number: str) -> bool:
    """
    Verify if the given number is a valid Indian phone number.

    Args:
    - number (str): Phone number to verify

    Returns:
    - bool: True if valid, otherwise False
    """

    # Regular expression pattern to match Indian phone numbers
    # pattern = r'^(\d{10,14}$'
    # print(bool(re.match(pattern, number)))
    print(len(number)<15)
    return len(number)<15

def sendwhatmsg_instantly(
    phone_no: str,
    message: str,
    wait_time: int = 15,
    tab_close: bool = False,
    close_time: int = 3,
) -> None:
    """Send WhatsApp Message Instantly"""

    if not core.check_number(number=phone_no):
        raise exceptions.CountryCodeException("Country Code Missing in Phone Number!")

    web.open(f"https://web.whatsapp.com/send?phone={phone_no}&text={quote(message)}")
    time.sleep(4)
    pg.click(core.WIDTH / 2, core.HEIGHT / 2)
    time.sleep(wait_time)
    pg.press("enter")
    log.log_message(_time=time.localtime(), receiver=phone_no, message=message)
    if tab_close:
        core.close_tab(wait_time=close_time)


def sendwhatmsg(
    phone_no: str,
    message: str,
    time_hour: int,
    time_min: int,
    wait_time: int = 15,
    tab_close: bool = False,
    close_time: int = 3,
) -> None:
    """Send a WhatsApp Message at a Certain Time"""

    if not core.check_number(number=phone_no):
        raise exceptions.CountryCodeException("Country Code Missing in Phone Number!")

    if time_hour not in range(25) or time_min not in range(60):
        raise Warning("Invalid Time Format!")

    current_time = time.localtime()
    left_time = datetime.strptime(
        f"{time_hour}:{time_min}:0", "%H:%M:%S"
    ) - datetime.strptime(
        f"{current_time.tm_hour}:{current_time.tm_min}:{current_time.tm_sec}",
        "%H:%M:%S",
    )

    if left_time.seconds < wait_time:
        raise exceptions.CallTimeException(
            "Call Time must be Greater than Wait Time as WhatsApp Web takes some Time to Load!"
        )

    sleep_time = left_time.seconds - wait_time
    print(
        f"In {sleep_time} Seconds WhatsApp will open and after {wait_time} Seconds Message will be Delivered!"
    )
    time.sleep(sleep_time)
    core.send_message(message=message, receiver=phone_no, wait_time=wait_time)
    log.log_message(_time=current_time, receiver=phone_no, message=message)
    if tab_close:
        core.close_tab(wait_time=close_time)


def sendwhatmsg_to_group(
    group_id: str,
    message: str,
    time_hour: int,
    time_min: int,
    wait_time: int = 15,
    tab_close: bool = False,
    close_time: int = 3,
) -> None:
    """Send WhatsApp Message to a Group at a Certain Time"""

    if time_hour not in range(25) or time_min not in range(60):
        raise Warning("Invalid Time Format!")

    current_time = time.localtime()
    left_time = datetime.strptime(
        f"{time_hour}:{time_min}:0", "%H:%M:%S"
    ) - datetime.strptime(
        f"{current_time.tm_hour}:{current_time.tm_min}:{current_time.tm_sec}",
        "%H:%M:%S",
    )

    if left_time.seconds < wait_time:
        raise exceptions.CallTimeException(
            "Call Time must be Greater than Wait Time as WhatsApp Web takes some Time to Load!"
        )

    sleep_time = left_time.seconds - wait_time
    print(
        f"In {sleep_time} Seconds WhatsApp will open and after {wait_time} Seconds Message will be Delivered!"
    )
    time.sleep(sleep_time)
    core.send_message(message=message, receiver=group_id, wait_time=wait_time)
    log.log_message(_time=current_time, receiver=group_id, message=message)
    if tab_close:
        core.close_tab(wait_time=close_time)


def sendwhatmsg_to_group_instantly(
    group_id: str,
    message: str,
    wait_time: int = 15,
    tab_close: bool = False,
    close_time: int = 3,
) -> None:
    """Send WhatsApp Message to a Group Instantly"""

    current_time = time.localtime()

    time.sleep(wait_time)
    core.send_message(message=message, receiver=group_id, wait_time=wait_time)
    log.log_message(_time=current_time, receiver=group_id, message=message)
    if tab_close:
        core.close_tab(wait_time=close_time)


def sendwhats_image(
    receiver: str,
    img_path: str,
    caption: str = "",
    wait_time: int = 15,
    tab_close: bool = False,
    close_time: int = 3,
) -> None:
    """Send Image to a WhatsApp Contact or Group at a Certain Time"""

    if (not receiver.isalnum()) and (not core.check_number(number=receiver)):
        raise exceptions.CountryCodeException("Country Code Missing in Phone Number!")

    current_time = time.localtime()
    core.send_image(
        path=img_path, caption=caption, receiver=receiver, wait_time=wait_time
    )
    log.log_image(_time=current_time, path=img_path, receiver=receiver, caption=caption)
    if tab_close:
        core.close_tab(wait_time=close_time)

def sendwhats_image_broadcast(        
    img_path: str,
    caption: str = "",
    wait_time: int = 15,
    tab_close: bool = False,
    close_time: int = 3,
) -> None:
    """Send Image to a WhatsApp Contact or Group at a Certain Time"""

    df = pd.read_csv("C:/Users/bhanu/Downloads/1.csv")


    message = """QLU( క్వాంటమ్ లైఫ్ యూనివర్సిటీ) మీకు విజయదశమి శుభాకాంక్షలు తెలియజేస్తుంది..      

  మీరు QLU ద్వారా  ఇప్పటికే సోల్ కోచ్ ట్రాన్స్ఫర్మేషన్ ప్రోగ్రాం(SCTP) చేసి ఉన్నారు.. ఈ కోర్స్ మీ ఆధ్యాత్మిక మార్గానికి ఎంతో సహాయపడిందని మేము  భావిస్తున్నాము.

   ఈ సంవత్సరం నుండి పది రోజులు పాటు మాత్రమే సోల్ కోచ్ ట్రాన్స్ఫర్మేషన్ ప్రోగ్రాం(SCTP - తెలుగు) నిర్వహించడం జరుగుతుంది. 
తేదీలు:
       15 నవంబర్ నుండి 24 నవంబర్ 2023 వరకు.

        25వ SCTP మన వికారాబాద్ QLU క్యాంపస్ లో  రెసిడెన్షియల్ కార్యక్రమానికి మీకు, మీ బంధుమిత్రులు అందరికీ ఇదే మా ప్రత్యేక ఆహ్వానం. 
 
       మన పూర్వపు స్టూడెంట్స్ ఎంతోమంది QLU క్యాంపస్ లో మరోసారి రెసిడెన్షియల్ ప్రోగ్రాం లో పాల్గొనాలనే ఆకాంక్షను..  ఈ 25వ sctp ప్రత్యేక కార్యక్రమంలో పాల్గొనేందుకు స్వాగతిస్తున్నాము. 
        మనందరం కలిసి మనం పొందిన ఆత్మజ్ఞానాన్ని అందరికీ  అందేలా కృషి చేద్దాము.. ఈ సోల్ కోచ్  కార్యక్రమం వివరాలు అందరికీ  తెలిసేలా చేద్దాం... 

SCTP - తెలుగులో  పాల్గొన్న వారి అనుభవాలు వారి మాటల్లో
https://youtu.be/aR9Q_Archbg

👉 ఈ కోర్సుకు హాజరవడానికి రిజిస్ట్రేషన్ తప్పనిసరి.
రిజిస్ట్రేషన్ చేసుకోవడానికి కింద లింక్ నొక్కండి
https://www.qluglobal.org/sctp-telugu-form
(పరిమిత సీట్లు మాత్రమే అందుబాటులో ఉన్నాయి) 

మరిన్ని వివరాల కోసం:
   📞  8184949723                                             soulcoach@qluglobal.org
    💻: www.qluglobal.org
"""

    for index, row in df.iterrows():
        print(row[0])
        caption = "Namaste "+row[0].capitalize()+" ji"+message
        # sendwhats_image("+919490913503", image_path, message)
        receiver = str(row[1])
        print(type(receiver))
        if not verify_indian_phone_number(receiver):
            continue
        

        if (not receiver.isalnum()) and (not core.check_number(number=receiver)):
            raise exceptions.CountryCodeException("Country Code Missing in Phone Number!")

        current_time = time.localtime()
        core.send_image(
            path=img_path, caption=caption, receiver=receiver, wait_time=wait_time
        )
        time.sleep(4)
        # log.log_image(_time=current_time, path=img_path, receiver=receiver, caption=caption)
        core.close_tab(wait_time=close_time)


        # if index == 10:
        #     break



def open_web() -> bool:
    """Opens WhatsApp Web"""

    try:
        web.open("https://web.whatsapp.com")
    except web.Error:
        return False
    else:
        return True

if __name__=="__main__":
    # df = pd.read_csv("C:/Users/bhanu/Downloads/1.csv")

    df = pd.read_csv("C:/Users/bhanu/Downloads/12.csv")

    image_path = "C:/Users/bhanu/Downloads/WhatsApp.jpeg"
    msg = """QLU( క్వాంటమ్ లైఫ్ యూనివర్సిటీ) మీకు విజయదశమి శుభాకాంక్షలు తెలియజేస్తుంది..      

  మీరు QLU ద్వారా  ఇప్పటికే సోల్ కోచ్ ట్రాన్స్ఫర్మేషన్ ప్రోగ్రాం(SCTP) చేసి ఉన్నారు.. ఈ కోర్స్ మీ ఆధ్యాత్మిక మార్గానికి ఎంతో సహాయపడిందని మేము  భావిస్తున్నాము.

   ఈ సంవత్సరం నుండి పది రోజులు పాటు మాత్రమే సోల్ కోచ్ ట్రాన్స్ఫర్మేషన్ ప్రోగ్రాం(SCTP - తెలుగు) నిర్వహించడం జరుగుతుంది. 
తేదీలు:
       15 నవంబర్ నుండి 24 నవంబర్ 2023 వరకు.

        25వ SCTP మన వికారాబాద్ QLU క్యాంపస్ లో  రెసిడెన్షియల్ కార్యక్రమానికి మీకు, మీ బంధుమిత్రులు అందరికీ ఇదే మా ప్రత్యేక ఆహ్వానం. 
 
       మన పూర్వపు స్టూడెంట్స్ ఎంతోమంది QLU క్యాంపస్ లో మరోసారి రెసిడెన్షియల్ ప్రోగ్రాం లో పాల్గొనాలనే ఆకాంక్షను..  ఈ 25వ sctp ప్రత్యేక కార్యక్రమంలో పాల్గొనేందుకు స్వాగతిస్తున్నాము. 
        మనందరం కలిసి మనం పొందిన ఆత్మజ్ఞానాన్ని అందరికీ  అందేలా కృషి చేద్దాము.. ఈ సోల్ కోచ్  కార్యక్రమం వివరాలు అందరికీ  తెలిసేలా చేద్దాం... 

SCTP - తెలుగులో  పాల్గొన్న వారి అనుభవాలు వారి మాటల్లో
https://youtu.be/aR9Q_Archbg

👉 ఈ కోర్సుకు హాజరవడానికి రిజిస్ట్రేషన్ తప్పనిసరి.
రిజిస్ట్రేషన్ చేసుకోవడానికి కింద లింక్ నొక్కండి
https://www.qluglobal.org/sctp-telugu-form
(పరిమిత సీట్లు మాత్రమే అందుబాటులో ఉన్నాయి) 

మరిన్ని వివరాల కోసం:
   📞  8184949723                                             soulcoach@qluglobal.org
    💻: www.qluglobal.org
"""

    for index, row in df.iterrows():
        print(row[0])
        receiver = str(row[1])
        if not verify_indian_phone_number(receiver):
            continue
        

        if (not receiver.isalnum()) and (not core.check_number(number=receiver)):
            raise exceptions.CountryCodeException("Country Code Missing in Phone Number!")

        # current_time = time.localtime()
        # core.send_image(
        #     path=image_path, caption=msg, receiver=receiver
        # )
        # time.sleep(4)
        # log.log_image(_time=current_time, path=img_path, receiver=receiver, caption=caption)
        # core.close_tab(wait_time=1)

        sendwhatmsg_instantly(receiver,msg, wait_time = 6,tab_close = True,close_time = 1)

    # sendwhats_image_broadcast(image_path)


    # for index, row in df.iterrows():
    #     message = "Namaste "+row['name']+message
    #     sendwhats_image("+919490913503", image_path, message)
    #     # sendwhats_image("row['phone'] +919490913503", "C:/Users/bhanu/Downloads/MS.jpg", "This is an automated image!")
    #     if index == 1:
    #         break
    


# import pywhatkit as pwk

# pwk.sendwhats_image("+919490913503", "C:/Users/bhanu/Downloads/MS.jpg", "This is an automated image!")
