
import unittest
from name_score import AnonymousName
class TestAnonymousName(unittest.TestCase):
    """Tests for the class AnonymousName"""

    def setUp(self):
        """
        Create a name and a set of score_name for use in all test methods
        """
        Name = "I don't know Rick"
        self.my_name = AnonymousName(Name)
        self.score_name = [0,10,1000]

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        Name = "I don't know Rick"
        #my_name = AnonymousName(Name)
        #my_name.store_response('English')
        #self.assertIn('English', my_name.score_name)
        self.my_name.store_response(self.score_name[0])
        self.assertIn(self.score_name[0],self.my_name.score_name)

    def test_store_three_score_name(self):
        Name = "I don't know Rick"
        my_name = AnonymousName(Name)
        score_name = [0,10,1000]

        for response in score_name:
            #my_name.store_response(response)
            self.my_name.store_response(response)

        for response in score_name:
            #self.assertIn(response,my_name.score_name)
            self.assertIn(response,self.my_name.score_name)

unittest.main()
