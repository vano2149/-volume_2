"""
Задачка из https://codewars.com/
"""
'''
def permutation(string):
    """
    не правильное пно прикольное Решение!
    """
    if not string:
        yield string
    else:
        for i in range(len(string)):
            rest = string[:i] + string[i + 1:]
            for x in permutation(rest):
                yield string[i:i+1] + x
    
list(permutation("spam"))
'''

from itertools import permutation as sperma
def permutations(string):
    """
    """
    return set([''.join(i) for i in sperma(string)])


from itertools import permutations as pm
permutations=lambda s: map(''.join, set(pm(s)))