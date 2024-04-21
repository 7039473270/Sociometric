from flask import Flask, render_template, request, jsonify
from ml_model.sentiment_analysis_model import analyze_sentiment # type: ignore

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('landing.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        tweet_text = request.form['tweet_text']
        sentiment = analyze_sentiment(tweet_text)
        return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
    app.run(debug=True)
