from flask import Flask, render_template, url_for, flash, request, redirect
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


app.config['SECRET_KEY'] = 'my_key'


def get_img_tag_list(response):
    soup = BeautifulSoup(response.text, 'html5lib')
    return soup.findAll('img')


def web_request(website):
    req = requests.get(url=website, headers=headers)
    return get_img_tag_list(req)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        img_list = web_request(form.website.data)
        return redirect(url_for("picture", img_list=img_list))
    return render_template("index.html", form=form)


@app.route('/picture', methods=['GET', 'POST'])
def picture():
    img_list = request.args.get('img_list')
    return render_template("pics.html", img_list=img_list)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
