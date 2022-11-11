import unittest


class EpitransTests(unittest.TestCase):

    def test_load_fr(self):
        import epitran
        epi = epitran.Epitran("fra-Latn")

    def test_transliteration(self):
        import epitran
        epi = epitran.Epitran("fra-Latn")
        transliteration = epi.transliterate(u'abandonnera')
        print(transliteration)
        #TODO add test

    def test_xsampa(self):
        import epitran
        epi = epitran.Epitran("fra-Latn")
        transliteration = epi.xsampa_list(u'abandonnera')
        transliteration = ''.join(transliteration)
        #TODO add test
    
    def test_xsampa_syllable(self):
        import epitran
        epi = epitran.Epitran("fra-Latn")
        transliteration = epi.xsampa_list(u'abandonnera')
        transliteration = ''.join(transliteration)
        from syllable_splitter.splitter import SyllabificationRules
        splitter = SyllabificationRules()
        split = splitter.syllabic_phonetics(transliteration)
        #self.assertIsNotNone(split)
        print(split)
        #self.assertEqual(split, ("a","b@","dO","nRa"))
        #TODO add test