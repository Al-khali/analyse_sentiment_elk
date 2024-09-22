import pytest
from pymongo import MongoClient
from src.data_storage.mongodb_handler import MongoDBHandler

@pytest.fixture
def mongo_client():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['test_database']
    yield db
    client.drop_database('test_database')
    client.close()

def test_insert_post(mongo_client):
    handler = MongoDBHandler(uri='mongodb://localhost:27017/', db_name='test_database')
    post_data = {
        'platform': 'facebook',
        'id': '123456',
        'message': 'Test message',
        'created_time': '2023-09-22T10:00:00',
        'topic': 'test topic'
    }
    result = handler.insert_post(post_data)
    assert result.inserted_id is not None
    
    # Verify the post was inserted
    inserted_post = mongo_client.posts.find_one({'id': '123456'})
    assert inserted_post is not None
    assert inserted_post['message'] == 'Test message'

def test_get_posts(mongo_client):
    handler = MongoDBHandler(uri='mongodb://localhost:27017/', db_name='test_database')
    # Insert some test data
    test_posts = [
        {'platform': 'facebook', 'id': '1', 'message': 'Test 1'},
        {'platform': 'instagram', 'id': '2', 'message': 'Test 2'}
    ]
    mongo_client.posts.insert_many(test_posts)
    
    # Test getting all posts
    all_posts = handler.get_posts()
    assert len(all_posts) == 2
    
    # Test getting posts with a query
    facebook_posts = handler.get_posts({'platform': 'facebook'})
    assert len(facebook_posts) == 1
    assert facebook_posts[0]['id'] == '1'

def test_update_post(mongo_client):
    handler = MongoDBHandler(uri='mongodb://localhost:27017/', db_name='test_database')
    # Insert a test post
    mongo_client.posts.insert_one({'id': '3', 'message': 'Original message'})
    
    # Update the post
    handler.update_post('3', {'message': 'Updated message'})
    
    # Verify the update
    updated_post = mongo_client.posts.find_one({'id': '3'})
    assert updated_post['message'] == 'Updated message'

def test_delete_post(mongo_client):
    handler = MongoDBHandler(uri='mongodb://localhost:27017/', db_name='test_database')
    # Insert a test post
    mongo_client.posts.insert_one({'id': '4', 'message': 'To be deleted'})
    
    # Delete the post
    handler.delete_post('4')
    
    # Verify the deletion
    deleted_post = mongo_client.posts.find_one({'id': '4'})
    assert deleted_post is None