from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# WebDriver'ı başlat
driver = webdriver.Chrome()
driver.get("https://www.google.com")

# Google'da "youtube" araması yap
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("youtube")
search_box.send_keys(Keys.RETURN)

# YouTube'a git
youtube_link = driver.find_element(By.PARTIAL_LINK_TEXT, "YouTube").get_attribute("href")
driver.get(youtube_link)

# YouTube'da arama yap
search_box_youtube = driver.find_element(By.NAME, "search_query")
search_box_youtube.send_keys("Veterinary Management System- Bitirme Projesi")
search_box_youtube.send_keys(Keys.RETURN)

# İlk videonun üzerine gelmek için bekleyin
time.sleep(3)
video_title_link = driver.find_element(By.CSS_SELECTOR, 'a.yt-simple-endpoint.ytd-video-renderer[title="Veterinary Management System-  Bitirme Projesi"]')
try:
    # Video başlığına tıklama deneyin
    video_title_link.click()
    time.sleep(2)
    print("Test passed")
except Exception as e:
    print("Test failed:", str(e))

# WebDriver'ı kapat
driver.quit()
