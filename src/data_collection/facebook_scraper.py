import time
from facebook_scraper import get_posts
from ..data_storage.mongodb_handler import MongoDBHandler
import os
from dotenv import load_dotenv

load_dotenv()

class FacebookScraper:
    def __init__(self, access_token=None):
        self.access_token = access_token
        self.db_handler = MongoDBHandler()

    def scrape_posts(self, page_id, topic, limit=100):
        try:
            count = 0
            for post in get_posts(page_id, pages=5):  # Limite à 5 pages pour éviter le blocage
                if count >= limit:
                    break
                if topic.lower() in post.get('text', '').lower():
                    post_data = {
                        'platform': 'facebook',
                        'id': post.get('post_id', ''),
                        'message': post.get('text', ''),
                        'created_time': post.get('time', ''),
                        'likes': post.get('likes', 0),
                        'comments': post.get('comments', 0),
                        'topic': topic
                    }
                    self.db_handler.insert_post(post_data)
                    count += 1
                time.sleep(1)  # Pause pour éviter le blocage
            print(f"Scraped and stored {count} Facebook posts related to '{topic}'")
        except Exception as e:
            print(f"Error scraping Facebook: {e}")

# Legacy functions for backward compatibility
def collect_facebook_data():
    facebook_pages = ["lejournaldelacote", "lejournalde"]  # Exemples de pages d'actualités françaises
    facebook_keywords = ["Jacques Chirac", "Chirac"]
    
    scraper = FacebookScraper()
    for page in facebook_pages:
        for keyword in facebook_keywords:
            scraper.scrape_posts(page, keyword)

if __name__ == "__main__":
    PAGE_ID = os.getenv('FACEBOOK_PAGE_ID')
    TOPIC = os.getenv('FACEBOOK_TOPIC')
    
    if not PAGE_ID or not TOPIC:
        print("FACEBOOK_PAGE_ID or FACEBOOK_TOPIC not found in .env file, using defaults")
        collect_facebook_data()
    else:
        scraper = FacebookScraper()
        scraper.scrape_posts(PAGE_ID, TOPIC)