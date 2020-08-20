from flask import Flask, render_template, url_for, flash, request, redirect
import requests
from forms import SearchForm
from image_scraper import scraper


app = Flask(__name__)

app.config['SECRET_KEY'] = 'my_key'

scraper_obj = scraper.Scraper()

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        scraper_obj.url = form.website.data
        return redirect(url_for("pictures"))
    return render_template("index.html", form=form)


@app.route('/pictures')
def pictures():
    image_src_list = scraper_obj.get_image_src_list()
    return render_template("pics.html", image_src_list=image_src_list)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
