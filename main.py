#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Phonetics project NLP M1: syllabification by Eduardo Calò and Thibo Rosemplatt"""

from collections import Counter

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
    return char in sampa_oral_vowels or char in sampa_nasal_vowels


def cv_orthographic(string):
    output = ''
    for char in string:
        if char in consonants:
            output += 'C'
        else:
            output += 'V'
    return output

def cv_phonetics(sampa):
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
    index_of_vowels = []
    for index in range(len(sampa)):
        if is_phonetic_vowel(sampa[index]):
            index_of_vowels.append(index)
    return index_of_vowels

def rules(string):
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
    position = int()
    if string[0] not in sampa_liquids and string[0] not in sampa_semi_vowels and (string[1] in sampa_liquids or string[1] in sampa_semi_vowels):
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
    breakpoint()
    position= int()
    if len(string)==3:
        if string[0] not in sampa_liquids and string[0] not in sampa_semi_vowels:
            if string[1] in sampa_liquids:
                if string[2] in sampa_semi_vowels:
                    position = 0
    
    do_this_rule = True
    for char in string:
        if char in sampa_liquids or char in sampa_semi_vowels:
            do_this_rule = False
    if do_this_rule:
        #go back on this 
        position = 1
    breakpoint()
    return position


def syllabic_phonetics(sampa):
    index_of_vowels = spot_vowels(sampa)
    
    slices = []
    
    index_of_hyphens_in_slices = []
    index_of_hyphens_total = []
    
    for number in range(1,len(index_of_vowels)):     
        current_slice = sampa[index_of_vowels[number-1]+1:index_of_vowels[number]]
        slices.append(current_slice)
    #get the position of the hyphens for each slice 
    for sl in slices:
        index_of_hyphens_in_slices.append(rules(sl))
    #get the positions of the hyphens for the whole word
    for i in range(len(index_of_hyphens_in_slices)):
        total_index = index_of_hyphens_in_slices[i] + index_of_vowels[i]+1
        index_of_hyphens_total.append(total_index)
    
    sampa = list(sampa)
    
    for index in reversed(index_of_hyphens_total):
        sampa.insert(index, '-')
    return ''.join(sampa)

def format_output(spelling, phonetic):
    output = '{} {} {} {} {} {}'.format(spelling,cv_orthographic(spelling),phonetic,cv_phonetics(phonetic),syllabic_phonetics(phonetic),cv_phonetics(syllabic_phonetics(phonetic)))
    return output
    
    
def main():
    process_file()


def process_file():
    #please make sure the file is in the same folder as the program
    final_output = ''
    with open('Input_File.txt','r') as input_file:
        lines = list(input_file) #split by lines
        for line in lines:
            line = line.replace('\n','')
            final_output += format_output(line.split(' ')[0],line.split(' ')[1])+'\n'
    with open('output_file.txt','w+') as output_file:
        print(final_output, file = output_file)
        

def get_all_CV_forms(filename = "output_file.txt"):
    with open('output_file.txt','r', encoding="utf-8-sig") as file:
       lines = file.read().split("\n")
       for i in range(len(lines)):
           lines[i] = lines[i].split(" ")
       cv_forms = [line[-1] for line in lines]
       cv_forms = [cv_form.split("-") for cv_form in cv_forms]
       cv_forms = [char for cv_form in cv_forms for char in cv_form]
       return cv_forms

def most_frequent(l):
    occurence_count = Counter(l)
    return occurence_count.most_common(15)

if __name__ == '__main__':
    main()
