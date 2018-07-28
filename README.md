# Reddit Comment App

Monitors a subreddit over time and displays the most used keywords in the subreddit.


For google-cloud-language:

- GOOGLE_CLOUD_PROJECT environment variable for the project you’d like to interact with
    - ie. `export GOOGLE_CLOUD_PROJECT="/path/to/keyfile.json"` in your current shell session
    - Generate the JSON file using these instructions: https://cloud.google.com/natural-language/docs/reference/libraries#client-libraries-install-pytho

- Gets the most used/popular terms and displays them in a word cloud. Bigger font, the more used/popular.

- Application Flow: 
    1. Enter a subreddit (search bar has list that automatically populates and can autocomplete)
    2. Pulls last 1000 comments from Reddit API and pass through NLP
    3. Load visualisation (async)
    4. spits out word cloud
    5. if search term is used again immediately after, block until 5 min have passed and just return the cached version instead