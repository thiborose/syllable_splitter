#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Phonetics project NLP M1:
Syllabification by Eduardo Calò and Thibo Rosemplatt
"""

from collections import Counter
import pandas

consonants = {'p', 't', 'k', 'b', 'd', 'g',
              'f', 's', 'c', 'v', 'z',
              'j', 'm', 'n', 'r', 'l', 'h'}

vowels = {'a', 'e', 'i', 'o', 'u', 'y', 'é', 'ê', 'ë', 'ï', 'à', 'ù'}

sampa_stop_consonants = {'p', 't', 'k', 'b', 'd', 'g'}
sampa_fricatives = {'f', 's', 'S', 'v', 'z', 'Z'}
sampa_liquids = {'R', 'l'}
sampa_nasals = {'m', 'n', 'N', 'G'}
sampa_semi_vowels = {'w', 'j', '8'}
sampa_oral_vowels = {'a', 'e', 'i', 'u', 'o', 'y', 'E', '9', '2', 'O', '*'}
sampa_nasal_vowels = {'@', '1', '5'}


def is_phonetic_vowel(char):
    """
    Takes a character as a string, 
    returns a Boolean (True if the character is a vowel, in the sampa alphabet)
    """
    return char in sampa_oral_vowels or char in sampa_nasal_vowels


def cv_orthographic(string):
    """
    Takes a string (orthographic writing), 
    returns the orthographic CV form as a string
    """
    output = ''
    for char in string:
        if char in consonants:
            output += 'C'
        else:
            output += 'V'
    return output


def cv_phonetics(sampa):
    """
    Takes a string (sampa), 
    returns the phonetic CV form as a string
    """
    output = ''
    for char in sampa:
        if is_phonetic_vowel(char):
            output += 'V'
        elif char == '-':
            output += char
        else:
            output += 'C'
    return output


def spot_vowels(sampa):
    """
    Takes a string (sampa), 
    returns the positions of the vowel sounds
    """
    index_of_vowels = []
    for index in range(len(sampa)):
        if is_phonetic_vowel(sampa[index]):
            index_of_vowels.append(index)
    return index_of_vowels


def rules(string):
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
        return rule2(string)
    if length >= 3:
        return rule3(string)


def rule2(string):
    """
    Takes a string (a 2-character phonetic sampa segment between 2 vowels), 
    return the position of the hyphen for syllabification,
    with application of the rule 2
    """
    position = int()
    if string[0] not in sampa_liquids and string[0] not in sampa_semi_vowels and (
            string[1] in sampa_liquids or string[1] in sampa_semi_vowels):
        position = 0
    elif string[0] in sampa_liquids and string[1] in sampa_liquids:
        position = 1
    elif string[0] in sampa_liquids and string[1] not in sampa_liquids and string[1] not in sampa_semi_vowels:
        position = 1
    elif string[0] in sampa_semi_vowels and not is_phonetic_vowel(string[1]):
        position = 1
    elif string[0] not in sampa_liquids and string[0] not in sampa_semi_vowels and string[1] not in sampa_liquids and string[1] not in sampa_semi_vowels:
        position = 1
    return position


def rule3(string):
    """
    Takes a string (a 3-or-more-character phonetic sampa segment between 2 vowels), 
    return a the position of the hyphen for syllabification
    with application of the rule 3
    """
    position = int()
    if len(string) >= 3:
        if string[0] not in sampa_liquids and string[0] not in sampa_semi_vowels:
            if string[1] in sampa_liquids:
                if string[2] in sampa_semi_vowels:
                    position = 0

    do_this_rule = True
    for char in string:
        if char in sampa_liquids or char in sampa_semi_vowels:
            do_this_rule = False
    if do_this_rule:
        # go back on this
        position = 1

    # to handle "floating s"
    if string[0] in sampa_stop_consonants and string[1] in sampa_fricatives and string[2] in sampa_stop_consonants:
        position = 2

    return position


def syllabic_phonetics(sampa):
    """
    Takes a sampa phonetic string, 
    returns a string:
    the sampa phonetic transcription splitted by syllables with hyphens
    """
    index_of_vowels = spot_vowels(sampa)

    slices = []

    index_of_hyphens_in_slices = []
    index_of_hyphens_total = []

    for number in range(1, len(index_of_vowels)):
        current_slice = sampa[index_of_vowels[number -
                                              1] + 1:index_of_vowels[number]]
        slices.append(current_slice)
    # get the position of the hyphens for each slice
    for sl in slices:
        index_of_hyphens_in_slices.append(rules(sl))
    # get the positions of the hyphens for the whole word
    for i in range(len(index_of_hyphens_in_slices)):
        total_index = index_of_hyphens_in_slices[i] + index_of_vowels[i] + 1
        index_of_hyphens_total.append(total_index)

    sampa = list(sampa)

    for index in reversed(index_of_hyphens_total):
        sampa.insert(index, '-')
    return ''.join(sampa)


def format_output(spelling, phonetic):
    """
    Takes the orthographic and phonetic form of a word, 
    returns a string containing:
        the orthographic form
        the CV form
        the phonetic form
        the syllabified phonetic form
        the syllabified CV form
    """
    output = '{} {} {} {} {} {}'.format(
        spelling,
        cv_orthographic(spelling),
        phonetic,
        cv_phonetics(phonetic),
        syllabic_phonetics(phonetic),
        cv_phonetics(
            syllabic_phonetics(phonetic)))
    return output


def main():
    """
    Main function, 
    launches the program
    """
    process_file()
    top15_all()


def process_file():
    """
    Processes the input file, produces the output file
    """
    # please make sure the file is in the same folder as the program
    final_output = ''
    with open('Input_File.txt', 'r', encoding='utf-8-sig') as input_file:
        print('input file read')
        lines = list(input_file)  # split by lines
        i = 0
        while i < len(lines):
            lines[i] = lines[i].replace('\n', '')
            # handling the double pronunciations
            if ";" in lines[i]:
                pronun1 = lines[i].split(";")[0]
                pronun2 = lines[i].split(" ")[0] + ' ' + lines[i].split(";")[1]
                del lines[i]
                lines.insert(i, pronun2)
                lines.insert(i, pronun1)
            final_output += format_output(lines[i].split(' ')[0], lines[i].split(' ')[1])
            if i != len(lines) - 1:
                final_output += '\n'
            i += 1
    with open('output_file.txt', 'w+') as output_file:
        print(final_output, file=output_file)
        print('output file written')


def get_all_CV_forms(filename="output_file.txt"):
    """
    Takes the path of the output file, 
    returns all the phonetic CV forms (each of them may appear multiple times)
    """
    with open('output_file.txt', 'r', encoding="utf-8-sig") as file:
        lines = file.read().split("\n")
        for i in range(len(lines)):
            lines[i] = lines[i].split(" ")
        cv_forms = [line[-1] for line in lines[:-1]]
        cv_forms = [cv_form.split("-") for cv_form in cv_forms]
        cv_forms = [char for cv_form in cv_forms for char in cv_form]
        return cv_forms


def get_all_macroclass_forms(filename="output_file.txt"):
    """
    Takes the path of the output file, 
    returns all the macroclass forms (each of them may appear multiple times)
    """

    macro_classes = {
        'fV': 'vzZ',
        'fU': 'fsSh',
        'stopV': 'bdg',
        'stopU': 'ptk',
        'n': 'mnNG',
        'l': 'Rl',
        'sv': 'wj8',
        'v': 'aeiuoyE92O*@15'
    }

    def get_macro_class(item):
        for k, v in macro_classes.items():
            if item in v:
                return k

    with open('output_file.txt', 'r', encoding="utf-8-sig") as file:
        lines = file.read().split("\n")
        for i in range(len(lines)):
            lines[i] = lines[i].split(" ")
        sampa_forms = [line[4] for line in lines[:-2]]
        sampa_forms = [sampa_form.split("-") for sampa_form in sampa_forms]
        sampa_forms = [
            char for sampa_form in sampa_forms for char in sampa_form]

        macro_forms = []

        for form in sampa_forms:
            this_form = ''
            try:
                for char in form:
                    this_form += get_macro_class(char)
                macro_forms.append(this_form)
            except(TypeError):
                print(char)
                print(form)
                pass

        return macro_forms


def get_all_plain_syllables(filename="output_file.txt"):
    """
    Takes the path of the output file, 
    returns all the phonetic syllables (each of them may appear multiple times)
    """
    with open('output_file.txt', 'r', encoding="utf-8-sig") as file:
        lines = file.read().split("\n")
        for i in range(len(lines)):
            lines[i] = lines[i].split(" ")
        syllables = [line[4] for line in lines[:-2]]
        syllables = [syllable.split("-") for syllable in syllables]
        syllables = [el for syllable in syllables for el in syllable]
        return syllables


def most_frequent(l):
    """
    Takes a list, 
    returns a list of 15 2-tuples:
        the first element of the tuple is an element of the list,
        the second is its number of occurence
    these 15 tuples are ordered decreasingly by number of apparition 
    of the list's element
    """
    occurence_count = Counter(l)
    return occurence_count.most_common(15)


def top15_all():
    """
    Creates a file containing the top 15 CV, macroclass, and phonetic forms. 
    """
    with open('top15.txt', 'w', encoding="utf-8-sig") as file:
        output = ''
        for func in [get_all_CV_forms, get_all_macroclass_forms,
                     get_all_plain_syllables]:
            data = pandas.DataFrame(most_frequent(func()))
            output += str(data) + '\n\n------------------\n\n'
            print('Top 15 for {}'.format(func.__name__))
            data.plot()

        print(output, file=file)
    print('Top15 file created ')


if __name__ == '__main__':
    main()
