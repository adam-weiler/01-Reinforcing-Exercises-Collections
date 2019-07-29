digits = ['1','2','3','4','5','6','7','8','9']
en = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
fr = ['un','deux','trois','quatre','cinq','six','sept','huit','neuf']
sp = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve']

def english_french_dictionary(digits, english, french, spanish):
    '''A function that takes several lists and assembles them 
    into a single dictionary.'''
    new_dictionary = {}

    for num, name in enumerate(digits):
        new_dictionary[num+1] = { 
            'english': en[num], 
            'french': fr[num], 
            'spanish': sp[num] 
        }
    
    return new_dictionary

new_dictionary = english_french_dictionary(digits, en, fr, sp)
print(new_dictionary)