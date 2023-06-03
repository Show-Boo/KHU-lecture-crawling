import time
import openpyxl
import requests
import csv

from bs4 import BeautifulSoup
from openpyxl import Workbook


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# 브라우저 꺼짐 방지 옵션
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

driver = webdriver.Chrome(options=chrome_options)

# 경희대학교 인포21 로그인
driver.get("https://info21.khu.ac.kr/com/LoginCtr/login.do?returnurl=https://portal.khu.ac.kr/ksign/index.jsp?ssoGb=ptfol&sso=ok")
driver.find_element(By.ID,'userId').send_keys('')         #id 기입
driver.find_element(By.ID,'userPw').send_keys('')         #pw 기입
driver.find_element(By.XPATH,"/html/body/form/div/div[2]/div[1]/div[2]/button[1]").click()
time.sleep(3.5) 


# 종합시간표 이동
driver.find_element(By.XPATH,"/html/body/header/article/nav/ul/li[2]/a").click()
driver.find_element(By.XPATH,"/html/body/header/article/nav/ul/li[2]/ul/li[1]/ul/li[2]/a[1]").click()
time.sleep(2)


# 캠퍼스 선택
driver.find_element(By.XPATH,"/html/body/div[6]/div/section/form/div[1]/ul/li[1]/dl[3]/dd/span/span/select").click()
driver.find_element(By.XPATH,"/html/body/div[6]/div/section/form/div[1]/ul/li[1]/dl[3]/dd/span/span/select/option[2]").click()
time.sleep(2)


# 단과대 선택 (# 일단 외국어대학만 불러옴)
driver.find_element(By.XPATH,"/html/body/div[6]/div/section/form/div[1]/ul/li[1]/dl[5]/dd/span/select").click()
driver.find_element(By.XPATH,"/html/body/div[6]/div/section/form/div[1]/ul/li[1]/dl[5]/dd/span/select/option[8]").click()
time.sleep(2)

"""
# 학과 선택
driver.find_element(By.XPATH,"/html/body/div[6]/div/section/form/div[1]/ul/li[1]/dl[6]/dd/span/select").click()
driver.find_element(By.XPATH,"/html/body/div[6]/div/section/form/div[1]/ul/li[1]/dl[6]/dd/span/select/option[4]").click()
time.sleep(2)


# 전공 선택
driver.find_element(By.XPATH,"/html/body/div[6]/div/section/form/div[1]/ul/li[1]/dl[7]/dd/span/select").click()
driver.find_element(By.XPATH,"/html/body/div[6]/div/section/form/div[1]/ul/li[1]/dl[7]/dd/span/select/option[2]").click()

time.sleep(2)
"""
driver.find_element(By.XPATH,"/html/body/div[6]/div/section/form/div[1]/ul/li[3]/a[1]/span").click()


#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

# csv 파일로 저장
f = open(r"C:\Users\USER\Desktop\crawl\selenium\data.csv", 'w', encoding = 'CP949', newline = '')
csvWriter = csv.writer(f)



# 크롤링
count = 0
while count < 5:
    for i in range(3,14):
        xpath = "/html/body/div[6]/div/section/ul[2]/li["
        xpath += str(i)
        xpath += "]/a"
        driver.find_element(By.XPATH,xpath).click()
        time.sleep(1)

        html =driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        lectures = soup.find_all('td', 'td_btn')
        arr = []
        index = 0
        for lecture in lectures:
            index+=1
            arr.append(lecture.text)
            print(arr)
            if(index==3):
                csvWriter.writerow(arr)
                arr = []
                index = 0
    


# csv 파일 닫기
f.close()


# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()



