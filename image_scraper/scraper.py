from bs4 import BeautifulSoup
import requests

class Scraper():

    def __init__(self, url=''):
        self.url = url
        self.headers = {
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'dnt': '1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'none',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-dest': 'document',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        }

    def get_request(self):
        """Places get request at url filled in the form
        """
        req = requests.get(self.url, headers=self.headers)
        return req

    def get_image_src_list(self):
        """gets image src tags and returns list of tags
        """

        soup = BeautifulSoup((self.get_request()).text, "html5lib")
        image_tags = soup.find_all('img')
        image_src_list = []
        for image_tag in image_tags:
            image_src_list.append(image_tag.get('src'))
        return image_src_list
