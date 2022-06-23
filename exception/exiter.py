"""
exiter.py file!
Перехват черезчур малого:
используйте категории на основе классов!
Page -> 390!
"""

import sys

def bye():
    sys.exit(40)

try:
    bye()
except:
    print('got it')
print('continuing...')