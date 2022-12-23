import os
import csv
import glob
import time
from O365 import Account
from selenium import webdriver
from selenium.webdriver.common.by import By
from openpyxl.workbook import Workbook

credentials = (
    "5f2bf0de-5d68-4c0a-833f-b32899de4579",
    "Xmv8Q~Kdk4wHu4ARgHOMRx8CVRwPZ.4gqe_4JcRD",
)
account = Account(
    credentials,
    auth_flow_type="credentials",
    tenant_id="d4295056-baca-4708-8c60-0351c0fb01db",
)


if account.authenticate():
    driver = webdriver.Firefox(
        executable_path="/home/abhishekraj/python/Python_Script/geckodriver"
    )
    driver.get(
        "https://security.microsoft.com/securitypoliciesandrules?tid=d4295056-baca-4708-8c60-0351c0fb01db"
    )
    driver.maximize_window()
    email = driver.find_element(By.NAME, "loginfmt")
    time.sleep(5)
    email.send_keys("Abhishek@jeeshanahmad2011outlook.onmicrosoft.com")
    time.sleep(5)
    driver.find_element(By.ID, "idSIButton9").click()
    pswd = driver.find_element(By.NAME, "passwd")
    pswd.send_keys("12345@Fdsa")
    time.sleep(5)
    signIn = driver.find_element(By.XPATH, "//input[@id='idSIButton9']").click()
    time.sleep(5)
    loginIn = driver.find_element(By.ID, "idSIButton9").click()
    time.sleep(10)
    back_to_all_policy = driver.find_element(
        By.XPATH, "//a[normalize-space()='Threat policies']"
    ).click()
    time.sleep(5)
    ############firstPolicy#############
    policy_number_first = driver.find_element(
        By.XPATH, "//button[normalize-space()='Anti-phishing']"
    ).click()
    time.sleep(5)
    policy_number_first_data = driver.find_elements(
        By.CLASS_NAME, "ms-DetailsRow-fields"
    )
    wb = Workbook()
    first_filepath="/home/abhishekraj/python/Python_Script/all_policy/Anti-phishing.xlsx"
    for data in policy_number_first_data:
        data.click()
        time.sleep(4)
        policy_first_data = driver.find_elements(
            By.CLASS_NAME, "ms-MetaDataItem"
        )
        print("file_name: ", data.text.splitlines()[0])
        ws1 = wb.create_sheet(data.text.splitlines()[0])
        for data in policy_first_data:
            print("file_key: ", data.text.splitlines()[0])
            print("file_value: ", data.text.splitlines()[1])
            sav_data = [data.text.splitlines()]
            for row in sav_data:
                ws1.append(row)
        time.sleep(4)
        close_btn = driver.find_element(
                By.XPATH, "//span[contains(text(),'Close')]"
            ).click()
    wb.save(filename = first_filepath)
    time.sleep(5)
    driver.back()
    time.sleep(5)
    ############secondPolicy#############
    inside_second_Policy_Folder = driver.find_element(
        By.XPATH, "//button[normalize-space()='Anti-spam']"
        ).click()
    time.sleep(5)
    second_Policy_Item = driver.find_elements(By.CLASS_NAME, "ms-DetailsRow-fields")
    second_filepath="/home/abhishekraj/python/Python_Script/all_policy/Anti-spam.xlsx"
    wb = Workbook()
    for data in second_Policy_Item:
        ws1 = wb.create_sheet(data.text.splitlines()[0])
        data.click()
        print("file_name",data.text.splitlines()[0])
        time.sleep(5)
        all_items = driver.find_elements(By.CLASS_NAME, "ms-MetaDataList")
        semi_final = []
        for res in all_items:
            second_policy_result = res.text.splitlines()
            print("key_1",res.text.splitlines()[0])
            print("value_1",res.text.splitlines()[1])
            semi_final.append(second_policy_result)
            sav_data = [res.text.splitlines()]
            for row in sav_data:
                ws1.append(row)
        wb.save(filename = second_filepath)
        time.sleep(3)
        try:
            button = driver.find_element(
                By.XPATH,
                "//button[@aria-label='Edit allowed and blocked senders and domains']",
            )
            time.sleep(5)
            if button.is_displayed():
                driver.execute_script("arguments[0].click();", button)
                get_data = driver.find_elements(
                    By.XPATH,
                    "//div[@id='fluent-default-layer-host']/div/div/div/div/div[2]/div[2]/div/div[4]/div/button",
                )
                time.sleep(5)
                for i in get_data:
                    i.click()
                    print("key_2",i.text.splitlines())
                    time.sleep(5)
                    items_ = driver.find_elements(
                        By.CLASS_NAME, "ms-DetailsList-contentWrapper"
                    )
                    for new_res in items_:
                        second_policy_ = new_res.text.splitlines()
                    print("value_2",second_policy_)
                    semi_final.append(second_policy_)
                    save_data = [i.text.splitlines(),second_policy_]
                    for row in save_data:
                        ws1.append(row)
                    wb.save(filename = second_filepath)
                    semi_final.append(second_policy_)
                    done_btn = driver.find_element(
                        By.XPATH, "//button[@aria-label='Done']"
                    ).click()
                time.sleep(5)
                cancel_btn = driver.find_element(
                    By.XPATH, "//i[@data-icon-name='Cancel']"
                ).click()
            time.sleep(5)
            close_btn = driver.find_element(
                By.XPATH, "//span[contains(text(),'Close')]"
            ).click()
        except:
            print("inside except")
            time.sleep(5)
            close_btn = driver.find_element(
                By.XPATH, "//span[contains(text(),'Close')]"
            ).click()
    time.sleep(5)
    
    secure_Score = driver.find_element(
        By.XPATH, "//a[@name='Secure score']"
    ).click()
    time.sleep(5)
    recomm_action = driver.find_element(
        By.XPATH, "//button[@aria-label='Recommended actions']"
    ).click()
    time.sleep(5)
    secure_Score = driver.find_element(
        By.XPATH, "//span[contains(text(),'Export')]"
    ).click()
    time.sleep(5)
    driver.quit()