from flask import Flask, render_template, url_for, flash, request
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)


headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }


def validate_url(url):
    regex = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    return regex.match(url)


@app.route('/', methods=['GET', 'POST'])
def index():
    default_site = "https://unsplash.com/s/photos/web"
    
    
    
    return render_template("index.html")


@app.route('/pictures')
def pictures():
    
    return render_template("pics.html")


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
