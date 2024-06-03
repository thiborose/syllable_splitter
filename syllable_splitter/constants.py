# X-SAMPA sets
CONSONANTS = {'p', 't', 'k', 'b', 'd', 'g',
              'f', 's', 'S', 'v', 'z',
              'Z', 'm', 'n', 'R', 'l', 'h'}

VOWELS = {'a', 'e', 'i', 'o', 'u', 'y', 'E', '2', '9', 'I', 'O', 'Y'}

SAMPA_STOP_CONSONANTS = {'p', 't', 'k', 'b', 'd', 'g'}
SAMPA_FRICATIVES = {'f', 's', 'S', 'v', 'z', 'Z'}
SAMPA_LIQUIDS = {'R', 'l'}
SAMPA_NASALS = {'m', 'n', 'N'}
SAMPA_SEMI_VOWELS = {'w', 'j', 'H'}
SAMPA_ORAL_VOWELS = {'a', 'e', 'i', 'u', 'o', 'y', 'E', '9', '2', 'O'}
SAMPA_NASAL_VOWELS = {'E~', '9~', 'a~', 'o~', 'u~', 'A~'}

MACRO_CLASSES = {
    'fV': 'vzZ',
    'fU': 'fsS',
    'stopV': 'bdg',
    'stopU': 'ptk',
    'n': 'mnN',
    'l': 'Rl',
    'sv': 'wjH',
    'v': 'aeiouyE29OIY'
}

ALL_SYMBOLS = CONSONANTS.union(VOWELS).union(SAMPA_STOP_CONSONANTS).union(SAMPA_FRICATIVES).union(SAMPA_LIQUIDS).union(SAMPA_NASALS).union(SAMPA_SEMI_VOWELS).union(SAMPA_ORAL_VOWELS).union(SAMPA_NASAL_VOWELS)