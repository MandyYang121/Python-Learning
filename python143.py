# download_chrome_143.py
import requests
import zipfile
import os
import sys
import platform

def download_chrome_143():
    system = platform.system().lower()
    
    # 根据系统选择下载链接
    urls = {
        'windows': 'https://storage.googleapis.com/chrome-for-testing-public/143.0.7499.192/win64/chrome-win64.zip',
        'darwin': 'https://storage.googleapis.com/chrome-for-testing-public/143.0.7499.192/mac-x64/chrome-mac-x64.zip',
        'linux': 'https://storage.googleapis.com/chrome-for-testing-public/143.0.7499.192/linux64/chrome-linux64.zip'
    }
    
    url = urls.get(system, urls['windows'])
    filename = f"chrome_143_{system}.zip"
    
    print(f"下载Chrome 143.0.7499.192...")
    response = requests.get(url, stream=True)
    
    with open(filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    
    print(f"下载完成，解压文件...")
    with zipfile.ZipFile(filename, 'r') as zip_ref:
        zip_ref.extractall("chrome_143")
    
    print(f"解压完成！")
    print(f"Chrome位置: {os.path.abspath('chrome_143')}")
    
    if system == 'windows':
        print(f"运行: chrome_143\\chrome-win64\\chrome.exe")
    elif system == 'darwin':
        print(f"运行: chrome_143/chrome-mac-x64/Google Chrome.app")
    else:
        print(f"运行: chrome_143/chrome-linux64/chrome")

if __name__ == "__main__":
    download_chrome_143()