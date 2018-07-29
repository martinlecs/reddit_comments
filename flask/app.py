from flask import Flask, jsonify
from reddit_comments.reddit.redditapi import *
from reddit_comments.nlp import *

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"


@app.route('/redditcomments/api/v1.0/subreddits', methods=['GET'])
def get_subreddits():
    return "List of Subreddits"


@app.route('/redditcomments/api/v1.0/comments/<string:subreddit>', methods=['GET'])
def get_comment_analysis(subreddit):

    # Check against list of valid Subreddits

    r = RedditAPI(subreddit)
    nlp = NLP()
    latest_comments = r.get_comment_stream(0)
    return jsonify(nlp.comment_batch_analysis(latest_comments))


if __name__  == "__main__":
    app.run(debug=True)