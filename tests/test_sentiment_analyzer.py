import pytest
from src.sentiment_analysis.sentiment_analyzer import SentimentAnalyzer

@pytest.fixture
def analyzer():
    return SentimentAnalyzer()

def test_positive_sentiment(analyzer):
    text = "I love this project! It's amazing and works perfectly."
    result = analyzer.analyze(text)
    assert result['sentiment'] == 'positive'
    assert result['sentiment_scores']['compound'] > 0

def test_negative_sentiment(analyzer):
    text = "This is terrible. I hate it and it doesn't work at all."
    result = analyzer.analyze(text)
    assert result['sentiment'] == 'negative'
    assert result['sentiment_scores']['compound'] < 0

def test_neutral_sentiment(analyzer):
    text = "The sky is blue. The grass is green."
    result = analyzer.analyze(text)
    assert result['sentiment'] == 'neutral'
    assert -0.05 <= result['sentiment_scores']['compound'] <= 0.05

def test_mixed_sentiment(analyzer):
    text = "I love the design, but the functionality is terrible."
    result = analyzer.analyze(text)
    # The overall sentiment could be positive, negative, or neutral
    # depending on the exact implementation, so we just check that it's analyzed
    assert 'sentiment' in result
    assert 'sentiment_scores' in result

def test_empty_text(analyzer):
    text = ""
    result = analyzer.analyze(text)
    assert result['sentiment'] == 'neutral'
    assert result['sentiment_scores']['compound'] == 0

def test_non_english_text(analyzer):
    text = "Je ne parle pas anglais."
    result = analyzer.analyze(text)
    # VADER might not accurately analyze non-English text,
    # but it should still return a result without raising an exception
    assert 'sentiment' in result
    assert 'sentiment_scores' in result