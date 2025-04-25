'''from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, func
from Database.Database import Base


class Districts(Base):
    __tablename__ = 'Districts'
    DistrictID = Column(Integer, primary_key=True, autoincrement=True)
    ProvinceID = Column(Integer, ForeignKey('Provinces.ProvinceID'))
    DistrictName = Column(String(50), unique=True, nullable=False)'''
import requests
from bs4 import BeautifulSoup
import mysql.connector
from Base import session
from Provinces import Province
from sqlalchemy.exc import IntegrityError

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0"}
'''conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="hien123",
    database="landinvest",
    port=3306, 
    auth_plugin='mysql_native_password'
)
cursor = conn.cursor()

response = requests.get("https://dauthau.asia/", headers=headers)
soup = BeautifulSoup(response.text, "lxml")
table = soup.find_all("div", class_="bidding-detail")
print(table)'''

chrome_service = Service(ChromeDriverManager().install())
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("incognito")
options.add_argument(f'user-agent={headers["User-Agent"]}')

driver = webdriver.Chrome(service=chrome_service, options=options)
driver.get("https://dauthau.asia/")
soup = BeautifulSoup(driver.page_source, "lxml")
provinces = soup.find("div", class_="relative_province map_province").find_all("path")
for province in provinces:
    new_province = Province(province_id=province.get("data-province"), name=province.get("data-tinh"))
    try:
        session.add(new_province)
        session.commit()
        print(f"Insert province: {province.get('data-tinh')} - ID: {province.get('data-province')}")
    except Exception as e:
        session.rollback()
        print(f"Error inserting province {province.get('data-tinh')} - ID: {province.get('data-province')}: {e}")
driver.quit()
    