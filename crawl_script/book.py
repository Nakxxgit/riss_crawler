import os, time, glob, shutil
from selenium import webdriver
from math import ceil
import re

def load_book(driver, page, keyword):

    url = 'http://www.riss.kr/search/Search.do?detailSearch=false&viewYn=OP&queryText=&iGroupView=5&icate=all&colName=bib_m&pageScale=1000&strSort=RANK&order=%2FDESC&query='
    url2 = '&iStartCount='

    driver.get(url+keyword+url2+str(page * 1000))

    while ': 0 건' in driver.find_element_by_xpath('//*[@id="level4_mainContent"]/form/div[1]/div/div/ul/li/span[2]').text:
        driver.refresh()
        driver.implicitly_wait(3)

    window_before = driver.window_handles[0]

    driver.find_element_by_xpath('//*[@id="allchk2"]').click()
    driver.find_element_by_xpath('//*[@id="level4_mainContent"]/form/div[3]/div[2]/div/div[1]/p[1]/span/a[1]').click()

    window_after = driver.window_handles[-1]
    driver.switch_to_window(window_after)
    driver.implicitly_wait(120)
    driver.find_element_by_xpath('//*[@id="radio-3"]').click()
    driver.find_element_by_xpath('//*[@id="radio-8"]').click()
    driver.find_element_by_xpath('/html/body/form/div/div[2]/div[5]/a[1]/img').click()
    time.sleep(30)

    driver.close()
    driver.switch_to_window(window_before)
    return

if __name__ == "__main__":
    f = open('keyword.txt', 'r')
    keyword = f.readline()
    f.close()
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome('./chromedriver.exe', chrome_options=options)
    driver.implicitly_wait(3)

    driver.get('http://www.riss.kr/search/Search.do?detailSearch=false&viewYn=OP&queryText=&iGroupView=5&icate=all&colName=bib_m&pageScale=1000&strSort=RANK&order=%2FDESC&query='+keyword+'&iStartCount='+str(0))
    results = driver.find_element_by_xpath('//*[@id="level4_mainContent"]/form/div[1]/div/div/ul/li/span[2]').text
    results = int(''.join(re.findall('\\d', results)))
    print('검색 결과:', results, '건')

    for i in range(ceil(results / 1000)):
        print(str(i * 1000))
        load_book(driver, i, keyword)

    download = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads')

    if not os.path.exists('../book'):
        os.mkdir('../book')
    for file in glob.glob(download + '/myCabinetExcelData*'):
        shutil.move(file, '../book')
    driver.quit()