import unittest
from app.models import Article


class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''

        self.new_article = Article("Emily Schultheis", "In major shift for Europe, Germany to spend $113B on defense - Associated Press", "BRUSSELS (AP) — Germany announced Sunday it was committing 100 billion euros ($113 billion) to a special armed forces fund and would keep its defense spending above 2% of GDP from now on", "https://apnews.com/article/russia-ukraine-business-europe-olaf-scholz-nato-91c93ef0dc7e759d202c0eee9c070ea5", "https://storage.googleapis.com/afs-prod/media/6f9dddee92e749409680ea5de4a64a57/3000.jpeg", "2022-02-27T14:15:00Z", "BRUSSELS (AP) Germany announced Sunday it was committing 100 billion euros ($113 billion) to a special armed forces fund and would keep its defense spending above 2% of GDP from now on. It was one of… [+5895 chars]")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))

