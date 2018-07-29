import praw
import yaml
import os

root_dir = os.path.dirname(os.path.dirname(__file__))


class NoPostsInSubredditError(Exception):
    pass


class InvalidLimitError(Exception):
    pass


class RedditAPI:

    def __init__(self, subreddit):
        self.__reddit = praw.Reddit(**self._getConfig())
        self.subreddit = subreddit

    def is_read_only(self):
        return self.__reddit.read_only

    def get_hottest_posts(self, limit=10):
        """
        :param subreddit: String
            Name of subreddit
        :param limit: Int
            Number of posts to retrieve
        :return: Submission
            Generator containing Submission objects
        """
        if limit < 0 or not isinstance(limit, int):
            raise InvalidLimitError("Limit must be of type Int and >= 0 ")
        try:
            submissions = self.__reddit.subreddit(self.subreddit).hot(limit=limit)
        except TypeError:
            raise
        return submissions

    def get_comment_stream(self, pause_after):
        """
        Yield new comments as they become available.

        Comments are yielded oldest first. Up to 100 historical comments will initially be returned.

        :pause_after:
            An integer representing the number of requests that result in no new items before this function yields None

        :return:
            Generator function containing Comment objects
        """
        return self.__reddit.subreddit(self.subreddit).stream.comments(pause_after=pause_after)

    def get_subreddits(self):
        """
            Gets list of all Subreddits on Reddit
        :return: list
        """
        #TODO: Have to scrape this information and update it using streams every now and then
        subreddits = []
        return subreddits


    @staticmethod
    def _getConfig():
        with open(os.path.join(root_dir, 'config.yaml'), 'r') as f:
            return yaml.load(f)

if __name__ == "__main__":
    r = RedditAPI('anime')
    latest_comments = r.get_comment_stream()

    for comment in latest_comments:
        if comment is None:
            break
        print(comment.body)
