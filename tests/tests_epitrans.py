import unittest


class EpitransTests(unittest.TestCase):

    def test_load_fr(self):
        import epitran
        epi = epitran.Epitran("fra-Latn")
