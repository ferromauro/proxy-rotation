import requests
from lxml import etree
from itertools import cycle

def main():
    proxies = proxy_list()
    proxy_pool = cycle(proxies)
    
    url = 'https://httpbin.org/ip'
    for i in range(1,16):
        proxy = next(proxy_pool)
        print(f'Request {i}')
        try:
            response = requests.get(url,proxies={"http": proxy, "https": proxy})
            print(response.json())
        except:
            print("Skipping. Proxy Not Responding")    
 
    
def proxy_list():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = etree.HTML(response.content)
    proxies = set()
    for i in parser.xpath('//*[@id="proxylisttable"]/tbody/tr')[:10]:
        if i.xpath('.//td[5][contains(text(),"elite proxy")]'):
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return(proxies)

if __name__ == '__main__':
    main()