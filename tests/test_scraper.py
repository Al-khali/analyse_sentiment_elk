import pytest
from unittest.mock import patch, MagicMock
from src.data_collection.facebook_scraper import FacebookScraper
from src.data_collection.instagram_scraper import InstagramScraper

@pytest.fixture
def mock_facebook_api():
    with patch('facebook.GraphAPI') as mock:
        yield mock

@pytest.fixture
def mock_instaloader():
    with patch('instaloader.Instaloader') as mock:
        yield mock

def test_facebook_scraper(mock_facebook_api):
    # Mock the Facebook API response
    mock_facebook_api.return_value.get_connections.return_value = {
        'data': [
            {
                'id': '1',
                'message': 'Test post about Jacques Chirac',
                'created_time': '2023-09-22T10:00:00+0000'
            }
        ]
    }
    
    scraper = FacebookScraper('fake_token')
    scraper.db_handler = MagicMock()  # Mock the database handler
    
    scraper.scrape_posts('test_page_id', 'Jacques Chirac')
    
    # Assert that the post was "stored" in the mocked database
    scraper.db_handler.insert_post.assert_called_once()
    stored_post = scraper.db_handler.insert_post.call_args[0][0]
    assert stored_post['id'] == '1'
    assert 'Jacques Chirac' in stored_post['message']

def test_instagram_scraper(mock_instaloader):
    # Mock an Instagram post
    mock_post = MagicMock()
    mock_post.shortcode = 'abc123'
    mock_post.caption = 'Test post about Jacques Chirac'
    mock_post.date_local.isoformat.return_value = '2023-09-22T10:00:00'
    mock_post.url = 'https://instagram.com/p/abc123'
    
    # Mock the Instaloader behavior
    mock_instaloader.return_value.context.get_hashtag_posts.return_value = [mock_post]
    
    scraper = InstagramScraper()
    scraper.db_handler = MagicMock()  # Mock the database handler
    
    scraper.scrape_posts('jacqueschirac', 'Jacques Chirac')
    
    # Assert that the post was "stored" in the mocked database
    scraper.db_handler.insert_post.assert_called_once()
    stored_post = scraper.db_handler.insert_post.call_args[0][0]
    assert stored_post['id'] == 'abc123'
    assert 'Jacques Chirac' in stored_post['message']
    assert stored_post['image_url'] == 'https://instagram.com/p/abc123'