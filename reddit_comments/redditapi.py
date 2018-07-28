import praw
import yaml
import os

root_dir = os.path.dirname(os.path.dirname(__file__))


class NoPostsInSubredditError(Exception):
    pass


class InvalidLimitError(Exception):
    pass


class RedditAPI:

    def __init__(self):
        self.__reddit = praw.Reddit(**self._getConfig())

    def is_read_only(self):
        return self.__reddit.read_only

    def get_hottest_posts(self, subreddit, limit=10):
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
            submissions = self.__reddit.subreddit(subreddit).hot(limit=limit)
        except TypeError:
            raise
        return submissions

    @staticmethod
    def _getConfig():
        with open(os.path.join(root_dir, 'config.yaml'), 'r') as f:
            config = yaml.load(f)
            return config

if __name__ == "__main__":
    r = RedditAPI()
    hot_anime = r.get_hottest_posts('anime', -1)
    print(hot_anime)
