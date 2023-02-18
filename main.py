import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchWindowException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# test

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options)
browser.get("https://info.bbdc.sg/members-login/")
browser.set_window_size(700, 700)
name = "Tom"
username = "0000000"
password = "0000000"

try:
    login_refresh = True
    while login_refresh:
        try:
            if EC.url_matches('https://info.bbdc.sg/members-login/?err=Please+refresh+your+browser+and+fill+in+the+fields'
                              '+properly+to+login.+' or 'https://info.bbdc.sg/members-login/'):
                browser.refresh()
                login_id_elem = browser.find_element(By.ID, 'txtNRIC')
                login_pw_elem = browser.find_element(By.ID, 'txtPassword')
                access_btn = browser.find_element(By.ID, 'loginbtn')
                login_id_elem.send_keys(username)
                login_pw_elem.send_keys(password)
                time.sleep(5)
                access_btn.click()
        except NoSuchElementException:
            login_refresh = False

    WebDriverWait(browser, 10).until(EC.url_matches('http://www.bbdc.sg/bbdc/bbdc_web/header2.asp'))
    send_anyway = browser.find_element(By.ID, 'proceed-button')
    send_anyway.click()

    # # Course Selection
    # p3_course = browser.find_element(By.CSS_SELECTOR, "input[value='P3|964000|0|G0000']")
    # p3_course.click()
    slot_submit_button = browser.find_element(By.CSS_SELECTOR, 'input[value="Submit"]')
    WebDriverWait(EC.element_to_be_clickable(slot_submit_button), 4)
    browser.execute_script("arguments[0].click();", slot_submit_button)

    # Home page
    frame_element = browser.find_element(By.XPATH, '//frame[@name="leftFrame"]')
    browser.switch_to.frame(frame_element)

    tp_booking = browser.find_element(By.XPATH, '/html/body/table/tbody/tr/td/table/tbody/tr[11]/td[3]/a')
    tp_booking.click()
    browser.switch_to.default_content()

    # TP Simulator page
    main_frame = browser.find_element(By.XPATH, '//frame[@name="mainFrame"]')
    browser.switch_to.frame(main_frame)

    sim_list = browser.find_elements(By.NAME, 'optTest')
    sim2_list = []
    for sim in sim_list:
        sim_list_val = sim.get_attribute("value")
        sim2_list.append(int(sim_list_val))
    max_sim = max(sim2_list)
    tp_sim_value = browser.find_element(By.XPATH, '//input[@value="' + str(max_sim) + '"]')
    tp_sim_value.click()
    submit_button = browser.find_element(By.NAME, 'btnSubmit')
    submit_button.click()

    # Select month
    mth_list = browser.find_elements(By.CSS_SELECTOR, "input#checkMonth")
    # for element in mth_list:
    #     mth_list_val = element.get_attribute('value')
    #     print(mth_list_val)

    month_list = []
    # jan = browser.find_element(By.XPATH, '//input[@value="Jan/2022"]')
    # jan.click()
    select_another_month = browser.find_element(By.XPATH, '//input[@value="Feb/2022"]')
    select_another_month.click()


    # Select Sessions & Days
    session_check = browser.find_element(By.NAME, 'allSes')
    session_check.click()
    days_check = browser.find_element(By.NAME, 'allDay')
    days_check.click()

    # Refresh for slots
    no_slot = True
    while no_slot:
        for num in range(60):
            search_button = browser.find_element(By.NAME, "btnSearch")
            WebDriverWait(EC.element_to_be_clickable(search_button), 10)
            search_button.click()
            try:
                noslot_back_button = browser.find_element(By.CSS_SELECTOR, 'input[name="btnBack"]')
            except NoSuchElementException:
                # Proceed with booking (make sure that it is at the booking page (implementation)
                slot_radio_info = browser.find_element(By.NAME, 'slot')
                slot_id = slot_radio_info.get_attribute('id')
                radio_button = browser.find_element(By.CSS_SELECTOR, 'input[id="' + str(slot_id) + '"]')
                radio_button.click()
                slot_submit_button = browser.find_element(By.CSS_SELECTOR, 'input[value="Submit"]')
                WebDriverWait(EC.element_to_be_clickable(slot_submit_button), 4)
                browser.execute_script("arguments[0].click();", slot_submit_button)
                double_cfm_button = browser.find_element(By.CSS_SELECTOR, 'input[value="Confirm"]')
                double_cfm_button.click()
                slot_found = "https://api.telegram.org/XXXXX:XXXXX/sendMessage" \
                             f"?chat_id=XXXXX&text=A slot has been found for {name}!! Swee Chai!"
                requests.get(slot_found)
            else:
                WebDriverWait(EC.element_to_be_clickable(noslot_back_button), 10)
                noslot_back_button.click()
        browser.refresh()
        frame_element = browser.find_element(By.XPATH, '//frame[@name="leftFrame"]')
        browser.switch_to.frame(frame_element)

        tp_booking = browser.find_element(By.XPATH, '/html/body/table/tbody/tr/td/table/tbody/tr[11]/td[3]/a')
        tp_booking.click()
        browser.switch_to.default_content()

        # TP Simulator page
        main_frame = browser.find_element(By.XPATH, '//frame[@name="mainFrame"]')
        browser.switch_to.frame(main_frame)

        tp_sim_value = browser.find_element(By.XPATH, '//input[@value="' + str(max_sim) + '"]')
        tp_sim_value.click()
        submit_button = browser.find_element(By.NAME, 'btnSubmit')
        submit_button.click()

        # Select month
        # jan = browser.find_element(By.XPATH, '//input[@value="Jan/2022"]')
        # jan.click()
        select_another_month = browser.find_element(By.XPATH, '//input[@value="Feb/2022"]')
        select_another_month.click()

        # Select Sessions & Days
        session_check = browser.find_element(By.NAME, 'allSes')
        session_check.click()
        days_check = browser.find_element(By.NAME, 'allDay')
        days_check.click()

except (NoSuchElementException, NoSuchWindowException):
    Chat_ID = "1919527854"
    bot_link = "https://api.telegram.org/XXXXXX/getUpdates"
    nse_restart = "https://api.telegram.org/XXxXX:XXXXX/sendMessage?chat_id" \
                   f"=XXXXX&text=The bot has stopped running for {name} due to NSE exception. Please restart. "
    requests.get(nse_restart)

else:
    restart_bot = "https://api.telegram.org/XXXXX:XXXX/sendMessage?chat_id" \
                  f"=XXXX&text=The bot has stopped running for {name} due to other reasons. Please restart. "
    requests.get(restart_bot)
