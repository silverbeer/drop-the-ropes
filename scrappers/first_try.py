from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://www.stratton.com/the-mountain/mountain-report#/')

lifts = driver.find_element_by_xpath('#main-col > div.trails-overview.full-width-container.dashboard-block.hide-tablet > div:nth-child(2) > div.col.data-block.main-block > div.block-text')
print(lifts)

time.sleep(5)
driver.quit()