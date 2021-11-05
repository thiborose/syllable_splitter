from .constants import *

class SyllabificationRules():
    def __init__(self):
        pass

    def get_sampa(self, word:str)->str:
        #TODO: write the function that turns text into phonetics
        pass

    def syllabic_phonetics(self, sampa:str):
        """
        sampa: sampa phonetic representation 
            -> list: sampa phonetic transcription splitted by syllables
        """
        index_of_vowels = self.spot_vowels(sampa)

        slices = []

        index_of_hyphens_in_slices = []
        index_of_hyphens_total = []

        for number in range(1, len(index_of_vowels)):
            current_slice = sampa[index_of_vowels[number -
                                                1] + 1:index_of_vowels[number]]
            slices.append(current_slice)
        # get the position of the hyphens for each slice
        for sl in slices:
            index_of_hyphens_in_slices.append(self.find_rule(sl))
        # get the positions of the hyphens for the whole word
        for i in range(len(index_of_hyphens_in_slices)):
            total_index = index_of_hyphens_in_slices[i] + index_of_vowels[i] + 1
            index_of_hyphens_total.append(total_index)

        sampa = list(sampa)

        for index in reversed(index_of_hyphens_total):
            sampa.insert(index, '-')
        
        split_sampa = ''.join(sampa).split("-")
        return tuple(split_sampa)

    def is_phonetic_vowel(self, char):
        """
        Takes a character as a string, 
        returns a Boolean (True if the character is a vowel, in the sampa alphabet)
        """
        return char in SAMPA_ORAL_VOWELS or char in SAMPA_NASAL_VOWELS

    def spot_vowels(self, sampa):
        """
        Takes a string (sampa), 
        returns the positions of the vowel sounds
        """
        index_of_vowels = []
        for index in range(len(sampa)):
            if self.is_phonetic_vowel(sampa[index]):
                index_of_vowels.append(index)
        return index_of_vowels

    def find_rule(self, string):
        """
        Takes a string (a phonetic sampa segment between 2 vowels), 
        returns the position of the hyphen for syllabification
        regardless the rule used
        """
        length = len(string)
        if length == 0:
            return 0
        if length == 1:
            return 0
        if length == 2:
            return self.rule_2(string)
        if length >= 3:
            return self.rule_3(string)


    def rule_2(self, string):
        """
        Takes a string (a 2-character phonetic sampa segment between 2 vowels), 
        return the position of the hyphen for syllabification,
        with application of the rule 2
        """
        position = int()
        if string[0] not in SAMPA_LIQUIDS and string[0] not in SAMPA_SEMI_VOWELS and (
                string[1] in SAMPA_LIQUIDS or string[1] in SAMPA_SEMI_VOWELS):
            position = 0
        elif string[0] in SAMPA_LIQUIDS and string[1] in SAMPA_LIQUIDS:
            position = 1
        elif string[0] in SAMPA_LIQUIDS and string[1] not in SAMPA_LIQUIDS and string[1] not in SAMPA_SEMI_VOWELS:
            position = 1
        elif string[0] in SAMPA_LIQUIDS and not self.is_phonetic_vowel(string[1]):
            position = 1
        elif string[0] not in SAMPA_LIQUIDS and string[0] not in SAMPA_SEMI_VOWELS and string[1] not in SAMPA_SEMI_VOWELS and string[1] not in SAMPA_SEMI_VOWELS:
            position = 1
        return position


    def rule_3(self, string):
        """
        Takes a string (a 3-or-more-character phonetic sampa segment between 2 vowels), 
        return a the position of the hyphen for syllabification
        with application of the rule 3
        """
        position = int()
        if len(string) >= 3:
            if string[0] not in SAMPA_LIQUIDS and string[0] not in SAMPA_SEMI_VOWELS:
                if string[1] in SAMPA_LIQUIDS:
                    if string[2] in SAMPA_SEMI_VOWELS:
                        position = 0

        do_this_rule = True
        for char in string:
            if char in SAMPA_LIQUIDS or char in SAMPA_SEMI_VOWELS:
                do_this_rule = False
        if do_this_rule:
            # go back on this
            position = 1

        # to handle "floating s"
        if string[0] in SAMPA_STOP_CONSONANTS and string[1] in SAMPA_FRICATIVES and string[2] in SAMPA_STOP_CONSONANTS:
            position = 2

        return position


    def sampa_split_to_cv_split(self, sampa:tuple):
        """
        Takes a tuple (sampa split), 
        returns the phonetic CV form as a string
        """
        return tuple([self.translate_sampa2cv(x) for x in sampa])

    def translate_sampa2cv(self, sampa_str:str)->str:

        cv = ''
        for char in sampa_str:
            if self.is_phonetic_vowel(char):
                cv += 'V'
            else:
                cv += 'C'
        return cv
