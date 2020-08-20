from bs4 import BeautifulSoup
import requests

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
}

def get_img_tag_list(response):
    soup = BeautifulSoup(response.text, 'html5lib')
    return soup.findAll('img')


def web_request(website):
    req = requests.get(url=website, headers=headers)
    return get_img_tag_list(req)

