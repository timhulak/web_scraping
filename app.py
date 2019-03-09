from flask import Flask, render_template, Markup, redirect
import mongo_storage
import datetime as dt


app = Flask(__name__)


@app.route('/')
def index():

    mars_scrape_output = mongo_storage.mongo_store()

    html_table = Markup(mars_scrape_output[0]['dataHtml'])
    headline = mars_scrape_output[0]['headline']
    teaser = mars_scrape_output[0]['teaser']
    featured_image = mars_scrape_output[0]['image']
    weather = mars_scrape_output[0]['weather']

    hem_img1_url = mars_scrape_output[0]['hemisphere'][0]['img_url']
    hem_img1 = mars_scrape_output[0]['hemisphere'][0]['title']

    hem_img2_url = mars_scrape_output[0]['hemisphere'][1]['img_url']
    hem_img2 = mars_scrape_output[0]['hemisphere'][1]['title']

    hem_img3_url = mars_scrape_output[0]['hemisphere'][2]['img_url']
    hem_img3 = mars_scrape_output[0]['hemisphere'][2]['title']

    hem_img4_url = mars_scrape_output[0]['hemisphere'][3]['img_url']
    hem_img4 = mars_scrape_output[0]['hemisphere'][3]['title']

    current_date = dt.datetime.now().strftime("%I:%M%p on %B %d, %Y")

    return render_template('index.html', html_table=html_table, headline=headline, teaser=teaser, featured_image=featured_image, hem_img1_url=hem_img1_url,hem_img1=hem_img1, hem_img2_url=hem_img2_url, hem_img2=hem_img2, hem_img3_url=hem_img3_url, hem_img3=hem_img3, hem_img4_url=hem_img4_url, hem_img4=hem_img4, weather=weather, current_date=current_date)


@app.route('/scrape')
def scrape():

    mars_scrape_output = mars_scrape_output = mongo_storage.mongo_store()

    return redirect("http://localhost:8889/", code=302)


if __name__ == '__main__':
    app.run(debug=True)
