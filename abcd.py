# Load selenium components
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import time
from urllib.request import urlopen
from lxml import etree

# Establish chrome driver and go to report site URL
url = "https://inout2020.devfolio.co/submissions"
driver = webdriver.Chrome()
driver.get(url)
for i in range(10):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
links=[]
for i in range(1,142):
    projects=driver.find_elements_by_xpath("//*[@id=\"__next\"]/div/div[2]/section/div/div/section/div[2]/div["+str(i)+"]/a")
    projects1=projects[0].get_attribute('href')
    links.append(projects1)
print(links)
public_funds=0
devfolio_funds=0
for j in links:
    response=urlopen(j)
    #driver.get(j)
    htmlparser=etree.HTMLParser()
    tree=etree.parse(response,htmlparser)
    pub_fund=((tree.xpath("//*[@id=\"root\"]/div/div[2]/section/div[2]/div[2]/div/div[3]/div[1]/span/span")[0].text))
    no=int((pub_fund).replace(',',''))
    #pub_fund=driver.find_elements_by_xpath("//*[@id=\"root\"]/div/div[2]/section/div[2]/div[2]/div/div[3]/div[1]/span/span")
    #no=int((pub_fund[0].text).replace(',',''))
    public_funds=no+public_funds
    dev_fund=((tree.xpath("//*[@id=\"root\"]/div/div[2]/section/div[2]/div[2]/div/div[3]/div[2]/span/span")[0].text))
    no2=int((dev_fund).replace(',',''))
    #dev_fund=driver.find_elements_by_xpath("//*[@id=\"root\"]/div/div[2]/section/div[2]/div[2]/div/div[3]/div[2]/span/span")
    #no2=int((dev_fund[0].text).replace(',',''))
    devfolio_funds=devfolio_funds+no2
print(public_funds)
print(devfolio_funds)
'''
#link_urls=[project.get_attribute('href') for project in projects] 
#print(link_urls)
page=requests.get(url)
print(page.content)
soup=BeautifulSoup(page.content,'html.parser')
results=soup.find(Class="Submissions___StyledDiv2-sc-122ppju-1 eLzJkH")
print(results.prettify())'''
print("Please enter current devfolio funds into your project")
abra=int(input())
print("Please enter the amount you want to check with")
cad=int(input())
print(((((((abra+public_funds)**0.5)+(cad**0.5)))**2)-public_funds-cad))
