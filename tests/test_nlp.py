import pandas as pd
import pytest
from reddit_comments.nlp import *


@pytest.fixture
def nlp():
    return NLP()


@pytest.fixture
def expected():
    data =  [('content', 0.028521, 0.0, 0.0),
            ('document', 0.078177, 0.0, 0.0),
            ('emotion', 0.076400, 0.0, 0.0),
            ('length', 0.012631, 0.0, 0.0),
            ('magnitude', 0.025579, 0.1, 0.1),
            ('score', 0.186451, 0.0, 0.0),
            ('sentiment', 0.257949, 0.0, 0.0),
            ('value', 0.021586, 0.0, 0.0)]
    return pd.DataFrame(data, columns=['name', 'salience', 'score', 'magnitude'])


def test_batch_comment(nlp, expected):
    text = ["The score of a document's sentiment indicates the overall emotion of a document. The magnitude of a document's sentiment indicates how much emotional content is present within the document, and this value is often proportional to the length of the document."]
    gen = (i for i in text)
    output = nlp.comment_batch_analysis(gen)
    print(output)
    print(expected)
    assert not pd.testing.assert_frame_equal(output, expected, check_less_precise=True)

