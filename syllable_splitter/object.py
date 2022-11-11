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
        self.sampa = splitter.get_sampa(self.word)
        self.cv = ""
        self.syllables_sampa = splitter.get_syllables_sampa()
        self.syllables_word = splitter.get_syllables_word()


    @property
    

    def __str__(self):
        return self.word