from selenium import webdriver
import time

chrome_driver_path = "C:\\Users\\Oscris\\Desktop\\chromedriver\\chromedriver.exe"  # path to chromedriver
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element_by_css_selector("#middle #cookie")

timeout = time.time() + 3
five_min = time.time() + 60*5

while True:
    cookie.click()
    if time.time() > timeout:
        find_upgrades = driver.find_elements_by_css_selector("#store b")
        upgrade_cost = [upgrade.text.split("-")[1].split()[0] for upgrade in find_upgrades if upgrade.text != ""]
        upgrade_cost = [int(item.replace(",","")) if "," in item else int(item) for item in upgrade_cost]
        for i in range(0,len(upgrade_cost)-1,1):
            money = int(driver.find_element_by_id("money").text.replace(",",""))
            if upgrade_cost[i] < money:
                n = i
        find_upgrades[n].click()
        timeout += 3

    if time.time() > five_min:
        cookie_per_s = driver.find_element_by_id("cps").text
        print(cookie_per_s)
        break
driver.quit()
