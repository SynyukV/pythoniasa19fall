"""
Assignment 1-A
==============
"""

this = ['house that Jack built.', 'malt', 'rat,', 'cat,', 'dog,',
        'cow with the crumpled horn,', 'maiden all forlorn,',
        'man all tatter\'d and torn,', 'priest all shaven and shorn,',
        'cock that crow\'d in the morn,', 'farmer sowing his corn,']

that = ['lay in', 'ate', 'killed', 'worried', 'tossed', 'milk\'d',
        'kissed', 'married', 'waked', 'kept']

for i in range(len(that)):
    that[i] = f'That {that[i]} the {this[i]}'

for i in range(len(this)):
    this[i] = f'This is the {this[i]}'

for i in range(len(this)):
    print(this[i])
    for j in range(i,0,-1):
        print(that[j-1])
    print()

    



