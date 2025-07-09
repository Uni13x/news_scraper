import chromedriver_autoinstaller
import pandas as pd
from bs4 import BeautifulSoup
from time import sleep
from datetime import datetime, timezone, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

chromedriver_autoinstaller.install()

# 1.ページを開く
driver = webdriver.Chrome()
driver.set_page_load_timeout(60)
driver.set_script_timeout(60)

try:
 driver.get("https://www.reuters.com/business/")
except TimeoutException:
  driver.execute_script("window.stop();")

driver.implicitly_wait(3)

sleep(3)

#2.「Load more articles」を押す
max_scrolls = 1
for i in range(max_scrolls):
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
  sleep(2)
  
  try:
    load_btn = driver.find_element(By.XPATH, "//button[.//span[text()='Load more articles']]")
    driver.execute_script("arguments[0].scrollIntoView(false);", load_btn)
    sleep(1)
    load_btn.click()
    sleep(2)
  except NoSuchElementException:
    print("クリック対象がない")
    break
  
sleep(3)

soup = BeautifulSoup(driver.page_source, "lxml")
articles = soup.find_all("div", {"data-testid": "MediaStoryCard"})

sleep(2)

data = []

for article in articles:
  heading = article.find(attrs={"data-testid":"Heading"})
  if heading is None:
    print("No heading")
    continue
  
  link = heading.select_one('a[data-testid="Link"]')
  if not link:
    link = article.find("a", href=True, attrs={"aria-hidden": "true"})
  if link is None:
    print("No link")
    continue
  
  title = heading.get_text(strip=True)
  url = "https://www.reuters.com/" + link["href"]
  
  time_tag = article.select_one('time[datetime]')
  if time_tag is None:
    print("No time_tag")
    continue
  iso_str = time_tag.get("datetime", "").strip()
  dt_utc = datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
  dt_jst = dt_utc.astimezone(timezone(timedelta(hours=9)))
  date_only = dt_jst.date()
  
  data.append({
    "title": title,
    "date": date_only,
    "url": url
  })
        
  print(f"{title} - {date_only} - {url}")
  sleep(4)

driver.quit()

# pandasでCSV出力
df = pd.DataFrame(data)
df.to_csv("reuters_business_articles.csv", index=False, encoding="UTF-8-sig")