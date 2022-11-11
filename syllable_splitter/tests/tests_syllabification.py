import unittest

sampa_test = "ab@dOnRa"

class TestImports(unittest.TestCase):
    def test_import_src(self):
        import syllable_splitter

    def test_import_constants(self):
        from syllable_splitter import constants 
        #print(constants.consonants)

    def test_import_splitter(self):
        import syllable_splitter.splitter

class TestSyllabification(unittest.TestCase):

    def test_sampa_phonetic_split(self):
        import syllable_splitter
        splitter = syllable_splitter.splitter.SyllabificationRules()
        split = splitter.syllabic_phonetics(sampa_test)
        #self.assertIsNotNone(split)
        print(split)
        self.assertEqual(split, ("a","b@","dO","nRa"))

    def test_sampa_split_to_cv_split(self):
        import syllable_splitter
        splitter = syllable_splitter.splitter.SyllabificationRules()
        cv_split = splitter.sampa_split_to_cv_split(("a","b@","dO","nRa"))
        print(cv_split)
        #self.assertIsNotNone(split)
        self.assertEqual(cv_split, ("V", "CV", "CV", "CCV"))

    



if __name__ == '__main__':
    unittest.main()