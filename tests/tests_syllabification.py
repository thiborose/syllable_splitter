import unittest

sampa_test = "ab@dOnRa"

class TestImports(unittest.TestCase):
    def test_import_src(self):
        import src

    def test_import_constants(self):
        from src import constants 
        #print(constants.consonants)

    def test_import_splitter(self):
        import src.splitter

class TestSyllabification(unittest.TestCase):

    def test_sampa_phonetic_split(self):
        import src
        splitter = src.splitter.SyllabificationRules()
        split = splitter.syllabic_phonetics(sampa_test)
        #self.assertIsNotNone(split)
        self.assertEqual(split, ("a","b@","dO","nRa"))

    def test_sampa_split_to_cv_split(self):
        import src
        splitter = src.splitter.SyllabificationRules()
        cv_split = splitter.sampa_split_to_cv_split(("a","b@","dO","nRa"))
        #self.assertIsNotNone(split)
        self.assertEqual(cv_split, ("V", "CV", "CV", "CCV"))

    



if __name__ == '__main__':
    unittest.main()