CONSONANTS = {'p', 't', 'k', 'b', 'd', 'g',
              'f', 's', 'c', 'v', 'z',
              'j', 'm', 'n', 'r', 'l', 'h'}

VOWELS = {'a', 'e', 'i', 'o', 'u', 'y', 'é', 'ê', 'ë', 'ï', 'à', 'ù'}

SAMPA_STOP_CONSONANTS = {'p', 't', 'k', 'b', 'd', 'g'}
SAMPA_FRICATIVES = {'f', 's', 'S', 'v', 'z', 'Z'}
SAMPA_LIQUIDS = {'R', 'l'}
SAMPA_NASALS = {'m', 'n', 'N', 'G'}
SAMPA_SEMI_VOWELS = {'w', 'j', '8'}
SAMPA_ORAL_VOWELS = {'a', 'e', 'i', 'u', 'o', 'y', 'E', '9', '2', 'O', '*'}
SAMPA_NASAL_VOWELS = {'@', '1', '5'}

MACRO_CLASSES = {
    'fV': 'vzZ',
    'fU': 'fsSh',
    'stopV': 'bdg',
    'stopU': 'ptk',
    'n': 'mnNG',
    'l': 'Rl',
    'sv': 'wj8',
    'v': 'aeiuoyE92O*@15'
}