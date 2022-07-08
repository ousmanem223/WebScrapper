import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/Users/tommy/Downloads/chromedriver_win32/chromedriver.exe")
driver.get('https://oxylabs.io/blog')
results = []
content = driver.page_source
soup = BeautifulSoup(content)
driver.quit()


for link in soup.find_all("a"):
    name = link.get("href")
    if name not in results:
        results.append(name)
df = pd.DataFrame({'Names': results})
df.to_csv('names.csv', index=False, encoding='utf-8')