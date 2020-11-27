import tkinter as tk
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

opts = Options()
opts.add_argument(
    "user-agent=Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36")
opts.add_argument('--start-maximized')
driver = webdriver.Chrome(executable_path=r"C:\chromedriver_win32\chromedriver.exe", options=opts)


def getCred():
    with open('credentials.txt', 'r') as cred:
        uid = cred.readline()
        pwd = cred.readline()

        return uid, pwd


def logIn(uid, pwd):
    driver.get("https://www.instagram.com/")
    user_id = driver.find_element_by_xpath('')
    user_pwd = driver.find_element_by_xpath('')
    user_id.send_keys(uid)
    user_pwd.send_keys(pwd)


def main():
    uid, pwd = getCred()
    logIn(uid, pwd)


if __name__ == '__main__':
    main()
