import time
from facebook_scraper import get_posts
import instaloader
from pymongo import MongoClient

# Configuration MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["social_media_data"]
facebook_collection = db["facebook_posts"]
instagram_collection = db["instagram_posts"]

# Configuration Facebook
facebook_pages = ["lejournaldelacote", "lejournalde"]  # Exemples de pages d'actualités françaises
facebook_keywords = ["Jacques Chirac", "Chirac"]

# Configuration Instagram
instagram_hashtags = ["jacqueschirac", "chirac"]

def collect_facebook_data():
    for page in facebook_pages:
        try:
            for post in get_posts(page, pages=5):  # Limite à 5 pages pour éviter le blocage
                if any(keyword.lower() in post['text'].lower() for keyword in facebook_keywords):
                    facebook_post = {
                        "text": post['text'],
                        "timestamp": post['time'],
                        "likes": post.get('likes'),
                        "comments": post.get('comments'),
                        "platform": "Facebook"
                    }
                    facebook_collection.insert_one(facebook_post)
                    print(f"Facebook post saved: {post['post_id']}")
        except Exception as e:
            print(f"Error collecting Facebook data from {page}: {str(e)}")
        time.sleep(5)  # Pause pour éviter le blocage

def collect_instagram_data():
    L = instaloader.Instaloader()
    for hashtag in instagram_hashtags:
        try:
            posts = instaloader.Hashtag.from_name(L.context, hashtag).get_posts()
            for post in posts:
                instagram_post = {
                    "text": post.caption,
                    "timestamp": post.date,
                    "likes": post.likes,
                    "comments": post.comments,
                    "platform": "Instagram"
                }
                instagram_collection.insert_one(instagram_post)
                print(f"Instagram post saved: {post.shortcode}")
                if instagram_collection.count_documents({}) >= 50:  # Limite à 50 posts
                    break
        except Exception as e:
            print(f"Error collecting Instagram data for #{hashtag}: {str(e)}")
        time.sleep(5)  # Pause pour éviter le blocage

if __name__ == "__main__":
    collect_facebook_data()
    collect_instagram_data()

    print(f"Total Facebook posts collected: {facebook_collection.count_documents({})}")
    print(f"Total Instagram posts collected: {instagram_collection.count_documents({})}")