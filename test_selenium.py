# test_selenium.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# 1. 自动下载并安装匹配的ChromeDriver
print("正在自动下载匹配的ChromeDriver...")
service = Service(ChromeDriverManager().install())

# 2. 启动浏览器
print("启动Chrome浏览器...")
driver = webdriver.Chrome(service=service)

# 3. 使用示例
try:
    driver.get("https://www.baidu.com")
    print(f"页面标题: {driver.title}")
    time.sleep(2)
finally:
    driver.quit()
    print("浏览器已关闭")