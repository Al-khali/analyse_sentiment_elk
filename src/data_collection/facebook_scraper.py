import facebook
from datetime import datetime
from data_storage.mongodb_handler import MongoDBHandler

class FacebookScraper:
    def __init__(self, access_token):
        self.graph = facebook.GraphAPI(access_token)
        self.db_handler = MongoDBHandler()

    def scrape_posts(self, page_id, topic, limit=100):
        try:
            posts = self.graph.get_connections(page_id, 'posts', limit=limit)
            for post in posts['data']:
                if topic.lower() in post.get('message', '').lower():
                    post_data = {
                        'platform': 'facebook',
                        'id': post['id'],
                        'message': post.get('message', ''),
                        'created_time': post['created_time'],
                        'topic': topic
                    }
                    self.db_handler.insert_post(post_data)
            print(f"Scraped and stored Facebook posts related to '{topic}'")
        except facebook.GraphAPIError as e:
            print(f"Error scraping Facebook: {e}")

if __name__ == "__main__":
    ACCESS_TOKEN = "YOUR_FACEBOOK_ACCESS_TOKEN"
    PAGE_ID = "PAGE_ID_TO_SCRAPE"
    TOPIC = "décès du président Jacques Chirac"
    
    scraper = FacebookScraper(ACCESS_TOKEN)
    scraper.scrape_posts(PAGE_ID, TOPIC)