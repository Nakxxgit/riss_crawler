from selenium import webdriver

url = 'http://www.riss.kr/search/Search.do?detailSearch=false&searchGubun=true&query='
keyword = '인성교육'

driver = webdriver.PhantomJS('./P')

driver.implicitly_wait(3)

driver.get(url + keyword)

driver.find_element_by_xpath('//*[@id="level4_mainContent"]/form/div[3]/ul/li[1]/div[1]/p[2]/a[1]')
//*[@id="level4_mainContent"]/form/div[3]/ul/li[1]/div[1]/p[2]/a[1]