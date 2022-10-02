from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pickle

result_file = open('result cbse 12th.txt','a')

stu_marks = {}
driver = webdriver.Chrome('C:/Users/user/PycharmProject/mydjango/misson pisa/chromedriver.exe')
driver.get("https://www.cbseresults.nic.in/class12/Class12th21.htm")
time.sleep(2)
if driver.current_url =='https://www.cbseresults.nic.in/class12/Class12th21.htm':
    driver.find_element_by_xpath('//*[@id="details-button"]').click()
    driver.find_element_by_xpath('//*[@id="proceed-link"]').click()
for i in range(25658116,25658196):
    driver.find_element_by_xpath('/html/body/table[3]/tbody/tr/td/font/center[2]/form/div[1]/center/table/tbody/tr[1]/td[2]/input').send_keys(i)
    driver.find_element_by_xpath('/html/body/table[3]/tbody/tr/td/font/center[2]/form/div[1]/center/table/tbody/tr[2]/td[2]/input').send_keys(84042)
    driver.find_element_by_xpath('/html/body/table[3]/tbody/tr/td/font/center[2]/form/div[1]/center/table/tbody/tr[3]/td/input[1]').click()
    page_source = driver.page_source
    soup = BeautifulSoup(page_source,'html.parser')
    print('\n'*10,'now td (data of student) comes\n')
    cs_practicles = {}
  # student information
    t1 = soup.find_all('table')[4].find_all('tbody')[0]
    for y in range(5):
        student_info= f"{t1.find_all('tr')[y].find_all('td')[0].text} = {t1.find_all('tr')[y].find_all('td')[1].text}"
        
        print(student_info)
        result_file.write(f'{student_info}\n')
  #headings
    head = soup.find_all('table')[5].find_all('tbody')[0].find_all('tr')[0]
    for j in range(6):
        headings = f"{head.find_all('td')[j].text} |"
        result_file.write(f'{headings}')
        print(headings,end='')
    print(end='\n')
