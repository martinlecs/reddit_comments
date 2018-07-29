# Unit tests using Pytest testing framework
import pytest
from reddit_comments.reddit.redditapi import *


@pytest.fixture
def reddit():
    return RedditAPI('anime')


def test_initialisation(reddit):
    assert reddit.is_read_only


@pytest.mark.parametrize("limit", [10,25,50,0])
def test_get_hottest_posts(reddit, limit):
    assert len([i for i in reddit.get_hottest_posts(limit)]) == limit


@pytest.mark.parametrize("limit, rounded", [(-1, 0), (1.5, 1), (.5, 1)])
def test_get_hottest_posts_invalid_limits(reddit, limit, rounded):
    with pytest.raises(InvalidLimitError):
        assert [i for i in reddit.get_hottest_posts(limit)] == rounded
