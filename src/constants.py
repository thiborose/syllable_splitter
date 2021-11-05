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