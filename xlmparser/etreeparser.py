"""
etreeparser.py file!
Page -> 458!
"""

from xml.etree.ElementTree import parse

tree = parse('mybooks.xml')
for E in tree.findall('title'):
    print(E.text)
