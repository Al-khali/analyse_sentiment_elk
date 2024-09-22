import instaloader
from data_storage.mongodb_handler import MongoDBHandler

class InstagramScraper:
    def __init__(self):
        self.L = instaloader.Instaloader()
        self.db_handler = MongoDBHandler()

    def scrape_posts(self, hashtag, topic, limit=100):
        try:
            posts = instaloader.Hashtag.from_name(self.L.context, hashtag).get_posts()
            count = 0
            for post in posts:
                if count >= limit:
                    break
                if topic.lower() in post.caption.lower():
                    post_data = {
                        'platform': 'instagram',
                        'id': post.shortcode,
                        'message': post.caption,
                        'created_time': post.date_local.isoformat(),
                        'image_url': post.url,
                        'topic': topic
                    }
                    self.db_handler.insert_post(post_data)
                    count += 1
            print(f"Scraped and stored {count} Instagram posts related to '{topic}'")
        except Exception as e:
            print(f"Error scraping Instagram: {e}")

if __name__ == "__main__":
    HASHTAG = "jacqueschirac"
    TOPIC = "décès du président Jacques Chirac"
    
    scraper = InstagramScraper()
    scraper.scrape_posts(HASHTAG, TOPIC)