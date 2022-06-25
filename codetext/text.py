"""
File text.py 
Page -> 428!
"""

#-*- coding: latin-1 -*-

myStr = 'ghbdnt'
myStr2 = 'A\u00cB4B\U000000e8C'
myStr3 = 'A' + chr(0xC4) + 'B' + chr(0xE8) + 'C'

import sys

print('Default encoding: ', sys.getdefaultencoding())

for aStr in myStr, myStr2, myStr3:
    print(f'{aStr}, strlen={len(aStr)}')

    bytes1 = aStr.encode()

    bytes2 = aStr.encode('latin-1')

    print(f'byteslen={len(bytes1)}, byteslen2={len(bytes2)}')