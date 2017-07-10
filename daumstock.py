import urllib2
from BeautifulSoup import BeautifulSoup as bs
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def get_historical_data(page):

    stockname = ""
    nowprice = ""
    sfprice = ""
    sinc = ""
    totprice = ""
    snum = ""
    frrate = ""

    data = []
    url = "http://finance.daum.net/quote/marketvalue.daum?stype=P&page=" + str(page) + "&col=listprice&order=desc"
    rows = bs(urllib2.urlopen(url).read()).findAll('table')[0].findAll('tr')

    for each_row in rows:
        divs = each_row.findAll('td')
        if not divs:
            divs = each_row.findAll('th')

        if len(divs) >= 7:
            if divs[1].find('a'):
                stockname = divs[1].find('a').text
            if divs[2]:
                nowprice = divs[2].text
            if divs[3]:
                sfprice = divs[3].text
            if divs[4]:
                sinc = divs[4].text
            if divs[5]:
                totprice = divs[5].text
            if divs[6]:
                snum = divs[6].text
            if divs[7]:
                frrate = divs[7].text

            print stockname + ":" + nowprice + ":" + sfprice + ":" + sinc + ":" + totprice + ":" + snum + ":" + frrate
            
for i in range(1,46):
    get_historical_data(i)
