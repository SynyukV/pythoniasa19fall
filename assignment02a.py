"""
Assignment 2-A
==============

Wrap Assignment 1-A in function `poem()` that satisfies the doctest:

>>> from pathlib import Path
>>> poem() == Path('data/poem-en.txt').read_text()
True
"""

def poem():
   
    this = ['house that Jack built.', 'malt', 'rat,', 'cat,', 'dog,',
            'cow with the crumpled horn,', 'maiden all forlorn,',
            'man all tattered and torn,', 'priest all shaven and shorn,',
            'cock that crowed in the morn,', 'farmer sowing his corn,']

    that = ['lay in', 'ate', 'killed', 'worried', 'tossed', 'milked',
            'kissed', 'married', 'waked', 'kept']

    a = ''

    for i in range(len(this)):
        a = a + f'This is the {this[i]}' + '\n'
        for j in range(i,0,-1):
            a = a + f'That {that[j-1]} the {this[j-1]}' + '\n'
        if i < len(this) - 1:
            a = a + '\n'
                
    return a

if __name__ == '__main__':
    import doctest
    doctest.testmod()

