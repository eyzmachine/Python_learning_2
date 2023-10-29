import requests as r
import re
from bs4 import BeautifulSoup as bs
import tldextract
from urllib.parse import urlparse


res = r.get("https://docs.python.org/3.5/")
print(res.status_code)
print(res.headers['Content-Type'])
with open("test.txt", "w") as f:
	print(res.content)
	q = res.content.decode()
	f.write(q)

res = r.get("https://docs.python.org/3.5/_static/py.png")
with open("test.png", "wb") as f:
	print(res.content)
	f.write(res.content)


def get_urls(url):
	res = r.get(url.replace('stepic.org', 'stepik.org'))
	dest_urls = list()
	if res.status_code == 200:
		root = bs(res.text, "html.parser")
		dest_urls = [x['href'].replace('stepic.org', 'stepik.org') for x in root.find_all('a')]
		return dest_urls
	return dest_urls

def check_url(url1, url2):
	urls = get_urls(url1)
	all_urls = list()
	for url in urls:
		all_urls.extend(get_urls(url))
	return url2 in all_urls

def two_clicks():
	url1 = input().replace('stepic.org', 'stepik.org')
	url2 = input().replace('stepic.org', 'stepik.org')
	return 'Yes' if check_url(url1, url2) else 'No'

# более грамотное решение на мой взгляд (потому что не используются ебучие регулярки для парса хтмла), но блиблиотека tldextract не котируется на степике PoroSad
# def get_urls2(url):
# 	res = r.get(url)
# 	dest_urls = list()
# 	if res.status_code == 200:
# 		root = bs(res.text, "html.parser")
# 		all_tags = root.find_all('a')
# 		for tag in all_tags:
# 			try:
# 				dest_urls.append(tag['href'])
# 			except:
# 				pass
# 		return dest_urls
# 	return dest_urls

# def get_unique_domains():
# 	url = input()
# 	url_list = list(map(str, get_urls2(url)))
# 	parsed_list = list(map(tldextract.extract, url_list))
# 	cleared_list = list(filter(lambda x: (x.suffix != '' and x.domain != ''), parsed_list))
# 	grouped_list = set([f"{x.subdomain}.{x.domain}.{x.suffix}" if x.subdomain != '' else f"{x.domain}.{x.suffix}" for x in cleared_list])
# 	print('\n'.join(sorted(grouped_list)))

def get_urls2(url):
	res = r.get(url)
	dest_urls = list()
	if res.status_code == 200:
		dest_urls = re.findall(r'<a.*href *= *[\"\']([\w\:\/\.\?\=\-\&\?\+]*)[\"\']', res.text)
	return dest_urls

def extract_domain(url):
	cutted = re.sub(r"((http://)|(https://)|(ftp://))?(.*)", r'\5', url)
	return cutted.split(':')[0].split('/')[0]

def get_unique_domains():
	url = input()
	url_list = list(map(str, get_urls2(url)))
	parsed_list = list(map(extract_domain, url_list))
	grouped_list = set(filter(lambda x: x != '..', parsed_list))
	print('\n'.join(sorted(grouped_list)))
	
url1 = 'https://pastebin.com/raw/hfMThaGb'
url2 = 'https://pastebin.com/raw/7543p0ns'
url3 = 'https://pastebin.com/raw/dbiMnN4d'
url4 = 'http://pastebin.com/raw/2mie4QYa'

get_unique_domains()