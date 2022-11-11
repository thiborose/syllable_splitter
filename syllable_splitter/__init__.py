from syllable_splitter.splitter import SyllabificationRules

rules = SyllabificationRules()

class Syllabed():
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
        self.sampa = rules.get_sampa(self.word)
        self.cv = ""
        self.syllables_sampa = rules.syllabic_phonetics(self.sampa)
        # self.syllables_word = rules.get_syllables_word()

    def __str__(self) -> str:
        return f"{self.word} -> {self.syllables_word}"

    def __repr__(self) -> str:
        return self.__str__()


def syllables(word:str, lang="french"):

    if lang != "french":
        raise NotImplementedError("french is currently the language available")

    assert isinstance(word, str), "word must be a string"

    return Syllabed(word=word)

if __name__  == '__main__':

    a = syllables("manteau")
    breakpoint()