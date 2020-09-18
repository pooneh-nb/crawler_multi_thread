# we want to crawl only the links belong to the mentioned url
from urllib.parse import urlparse

#Get domain name (example.com)
def get_domain_name(url):
    try:
        results = get_subdomain_name(url).split('.')
        return results[-2]+ '.' +results[-1]
    except:
        return ''
# Get sub domain name (name.example.com)
def get_subdomain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''

print(get_domain_name('https://www.programiz.com/python-programming/methods/built-in/staticmethod'))