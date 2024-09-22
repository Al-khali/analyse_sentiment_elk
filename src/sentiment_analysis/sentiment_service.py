from flask import Flask, request, jsonify
from sentiment_analyzer import SentimentAnalyzer
from loguru import logger
from werkzeug.exceptions import BadRequest

app = Flask(__name__)
analyzer = SentimentAnalyzer()

@app.route('/analyze_sentiment', methods=['POST'])
def analyze_sentiment():
    try:
        data = request.get_json(force=True)
        if not data or 'text' not in data:
            raise BadRequest('No text provided')
        
        text = data['text']
        logger.info(f"Analyzing sentiment for text: {text[:50]}...")
        
        result = analyzer.analyze(text)
        logger.info(f"Sentiment analysis result: {result}")
        
        return jsonify(result), 200
    except BadRequest as e:
        logger.error(f"Bad request: {str(e)}")
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        logger.exception(f"An error occurred: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    logger.add("sentiment_service.log", rotation="500 MB")
    logger.info("Starting Sentiment Analysis Service")
    app.run(debug=False, host='0.0.0.0', port=5000)