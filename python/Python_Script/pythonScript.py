import csv
import time
from O365 import Account
from selenium import webdriver
from selenium.webdriver.common.by import By

credentials = ('5f2bf0de-5d68-4c0a-833f-b32899de4579',
               'Xmv8Q~Kdk4wHu4ARgHOMRx8CVRwPZ.4gqe_4JcRD')
account = Account(credentials, auth_flow_type='credentials',
                  tenant_id='d4295056-baca-4708-8c60-0351c0fb01db')

if account.authenticate():
    driver = webdriver.Firefox(
        executable_path="/home/abhishekraj/python/Python_Script/geckodriver")
    driver.get(
        'https://security.microsoft.com/securitypoliciesandrules?tid=d4295056-baca-4708-8c60-0351c0fb01db')
    driver.maximize_window()
    email = driver.find_element(By.NAME, 'loginfmt')
    email.send_keys('Abhishek@jeeshanahmad2011outlook.onmicrosoft.com')
    driver.find_element(By.ID, 'idSIButton9').click()
    pswd = driver.find_element(By.NAME, 'passwd')
    pswd.send_keys('12345@Fdsa')
    time.sleep(2)
    signIn = driver.find_element(By.XPATH, "//input[@id='idSIButton9']").click()
    time.sleep(2)
    loginIn = driver.find_element(By.ID, "idSIButton9").click()
    time.sleep(8)
    policy_Folder = driver.find_element(
        By.XPATH, "//a[normalize-space()='Threat policies']").click()
    time.sleep(8)
    inside_Policy_Folder = driver.find_element(
        By.XPATH, "//button[normalize-space()='Anti-spam']").click()
    time.sleep(8)
    Policy_first = driver.find_element(
        By.XPATH, "//span[@title='Anti-spam inbound policy (Default)']").click()

    all_items = driver.find_elements(By.CLASS_NAME, 'ms-MetaDataItem')
    a = all_items.text()
    print(a)
    final_ = []
    for res in all_items:
        result = res.text.splitlines()
        final = final_.append(result)

    with open("csvfile.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(['Anti-spam inbound policy (Default)'])
        writer.writerows(final_)
    driver.quit()
