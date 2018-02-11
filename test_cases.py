import unittest
from twitter_boggle import *

class TestCases(unittest.TestCase):
    def test_CommonWords(self):
        # clear order
        d1 = {'quick':6, 'brown':5, 'fox':4, 'jumped':3, 'over':2, 'lazy':1, 'dog':1}
        d2 = {'quick':6, 'brown':5, 'fox':4, 'jumped':3, 'over':2, 'lazy':1, 'dog':1}
        dicts = {'d1':d1, 'd2':d2}
        self.assertEqual(most_common_shared_words(dicts), ['quick', 'brown', 'fox', 'jumped', 'over'], "Should return the top 5")

        # first list is longer
        d1 = {'quick':6, 'brown':5, 'fox':4, 'jumped':3, 'over':2, 'lazy':1, 'dog':1, 'hello':4}
        d2 = {'quick':6, 'brown':5, 'fox':4, 'jumped':3, 'over':2, 'lazy':1, 'dog':1}
        dicts = {'d1':d1, 'd2':d2}
        self.assertEqual(most_common_shared_words(dicts), ['quick', 'brown', 'fox', 'jumped', 'over'], "list size should not matter")

        # second list is longer
        d1 = {'quick':6, 'brown':5, 'fox':4, 'jumped':3, 'over':2, 'lazy':1, 'dog':1}
        d2 = {'quick':6, 'brown':5, 'fox':4, 'jumped':3, 'over':2, 'lazy':1, 'dog':1, 'hello':4}
        dicts = {'d1':d1, 'd2':d2}
        self.assertEqual(most_common_shared_words(dicts), ['quick', 'brown', 'fox', 'jumped', 'over'], "list size should not matter")

        # one list has more highly ranked words
        d1 = {'quick':60, 'brown':50, 'fox':40, 'jumped':30, 'over':2, 'lazy':1, 'dog':1}
        d2 = {'quick':6, 'brown':5, 'fox':4, 'jumped':3, 'over':2, 'lazy':1, 'dog':1}
        dicts = {'d1':d1, 'd2':d2}
        self.assertEqual(most_common_shared_words(dicts), ['quick', 'brown', 'fox', 'jumped', 'over'], "rank should be added")

        # each list has different high ranked words
        d1 = {'quick':60, 'brown':5, 'fox':4, 'jumped':30, 'over':2, 'lazy':1, 'dog':1}
        d2 = {'quick':6, 'brown':50, 'fox':40, 'jumped':3, 'over':2, 'lazy':1, 'dog':1}
        dicts = {'d1':d1, 'd2':d2}
        self.assertEqual(most_common_shared_words(dicts), ['quick', 'brown', 'fox', 'jumped', 'over'], "rank should be added")

        # lists are out of order
        d1 = {'lazy':1, 'quick':6, 'jumped':3, 'over':2,  'brown':5, 'dog':1, 'fox':4}
        d2 = {'lazy':1, 'quick':6, 'jumped':3, 'over':2,  'brown':5, 'dog':1, 'fox':4}
        dicts = {'d1':d1, 'd2':d2}
        self.assertEqual(most_common_shared_words(dicts), ['quick', 'brown', 'fox', 'jumped', 'over'], "order of lists should not matter")

        # the lists only share 1 common word
        d1 = {'quick':6, 'brown':5, 'fox':4, 'jumped':3, 'over':2, 'lazy':2, 'dog':1}
        d2 = {'quick':1, 'pack':6, 'my':5, 'box':4, 'five':3, 'dozen':3, 'liquor':2, 'jugs':1}
        dicts = {'d1':d1, 'd2':d2}
        self.assertEqual(most_common_shared_words(dicts), ['quick'])

        # the lists have no words in common
        d1 = {'quick':6, 'brown':5, 'fox':4, 'jumped':3, 'over':2, 'lazy':2, 'dog':1}
        d2 = {'pack':6, 'my':5, 'box':4, 'five':3, 'dozen':3, 'liquor':2, 'jugs':1}
        dicts = {'d1':d1, 'd2':d2}
        self.assertEqual(most_common_shared_words(dicts), [])

unittest.main(verbosity=2)
