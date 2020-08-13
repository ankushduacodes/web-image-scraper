from flask import Flask, render_template, url_for, flash, request
import requests
from forms import SearchForm
from bs4 import BeautifulSoup
app = Flask(__name__)


headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
}


default_site = "https://unsplash.com/s/photos/web"


def get_src_tag(response):
    soup = BeautifulSoup(response.content, "html5lib")
    


def web_request(website):
    try:
        req = requests.get(website, headers=headers)
        req.raise_for_status()
    except HTTPError:
        return []
    
    return get_src_tag(req)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    if form.validate_on_submit() and web_request(form.website.data):
            return redirect(url_for("pics.html", src=src))
        
    return render_template("index.html", form=form)


@app.route('/pictures')
def pictures():
    
    return render_template("pics.html")


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
