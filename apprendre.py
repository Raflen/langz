import random
import json
from IPython.display import clear_output

def rev_dict(d):
    '''Swap values and keys.'''    
    return {v: k for k, v in d.items()}

def check_me(d):
    tough_ones = {}
    items=list(d.items()) # List of tuples
    random.shuffle(items)
    for key, value in items:
        print(key)
        answer = input('Translate: ')
        if answer == value:
            print('Fine')
        else:
            print(value)
            tough_ones[key] = value
    print('You are somewhat done.')
    if tough_ones:
        print('keep going.')
        check_me(tough_ones)   
    else:
        print('Finish.')

def read_words(fname):
    with open(fname, 'r') as f:
        d = json.load(f)
    return d

def check_enter(d):
    items=list(d.items()) # List of tuples
    random.shuffle(items)
    for key, value in items:        
        print(key)
        input()        
        print(value)
        input()
        clear_output()
    print('And u done.')