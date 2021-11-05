from splitter import SyllabificationRules

splitter = SyllabificationRules()

class Object():
    """
    Parses an input string, 
    creates an object containing the different features
        - CV syllabification
        - Syllabification
        - Phonetic representation 
        - Phonetic syllabification
    """
    def __init__(self, word:str) -> None:
        assert isinstance(word, str) , "word must be a str"
        self.word = word
        self.phonemes = self._get_phonemes()
        self.cv = self._get_cv()
        self.syllables = self._get_syllables()
    
    def _get_phonemes(self)->list:
        pass

    def _get_cv(self)->list:
        pass

    def _get_syllables(self)->list: 
        pass

    def __str__(self):
        return self.word