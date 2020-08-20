from flask import Flask, render_template, url_for, flash, request, redirect
import requests
from forms import SearchForm
from image_scraper.scraper import *


app = Flask(__name__)

app.config['SECRET_KEY'] = 'my_key'

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
