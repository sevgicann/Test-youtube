import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# WebDriver'ı başlat
driver = webdriver.Chrome()
driver.get("https://www.google.com")

# Google arama kutusuna "youtube" yazın ve Enter tuşuna basın
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("youtube")
search_box.send_keys(Keys.RETURN)

# YouTube arama sonuçları sayfasından YouTube ana sayfasına gidin
youtube_link = driver.find_element(By.PARTIAL_LINK_TEXT, "YouTube").get_attribute("href")
driver.get(youtube_link)

# YouTube ana sayfasında arama kutusuna "test otomasyonu" yazın ve Enter tuşuna basın
search_box_youtube = driver.find_element(By.NAME, "search_query")
search_box_youtube.send_keys("test otomasyonu")
search_box_youtube.send_keys(Keys.RETURN)
time.sleep(3)

# Başarılı veya başarısız olduğunu belirtmek için çıktı ekle
try:
    # Eğer arama sonuçları sayfasında "test otomasyonu" bulunuyorsa, test başarılıdır
    assert "test otomasyonu" in driver.page_source
    print("Test passed")
except AssertionError:
    # Aksi halde test başarısızdır
    print("Test failed")

# WebDriver'ı kapat
driver.quit()
