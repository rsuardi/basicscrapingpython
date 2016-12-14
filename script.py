from bs4 import BeautifulSoup
import urllib

thepage = urllib.urlopen('https://support.hockeyapp.net/kb/client-integration-ios-mac-os-x-tvos/ios-device-types').read()
soup = BeautifulSoup(thepage,"html.parser")

class ProductType(object):
    device_type = ""
    product_name = ""

def make_product_type(device_type,product_name):
    product = ProductType()
    product.device_type = device_type
    product.product_name = product_name
    return product

product_type_list = []

for rows in soup.findAll('div',{'class':'article'})[1].find('table').findAll('tr'):
    column = rows.findAll('td')
    if(column != []):
        obj = make_product_type(column[0].text, column[1].text)
        product_type_list.append(obj)

for p in product_type_list:
    print(p.device_type + ','+ p.product_name)