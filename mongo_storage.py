import pymongo
import scrape_mars


def mongo_coll():
    featured_image_url = scrape_mars.img()
    mars_weather = scrape_mars.weather()
    df_table_html = scrape_mars.facts()
    hemisphere_image_urls = scrape_mars.hem()
    news_title, news_p = scrape_mars.news()
    df_table_html = scrape_mars.facts()

    #Connection
    conn = 'mongodb://localhost:8889'
    client = pymongo.MongoClient(conn)

    # Mongo DB
    db = client.marsdb
    db.mars.drop()
    
    post = {
        'headline': news_title,
        'teaser': news_p,
        'image': featured_image_url,
        'hemisphere': hemisphere_image_urls,
        'dataHtml': df_table_html,
        'weather': mars_weather
    }

    db.mars.insert_one(post)
    
    mars_output = list(db.mars.find())
    return mars_output


if __name__ == '__main__':
    mongo_coll()
