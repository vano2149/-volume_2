"""
Complete the solution so that it strips all text 
that follows any of a set of comment markers passed in. 
Any whitespace at the end of the 
line should also be stripped out.
"""
def solution(string,markers):
    s = string.split("\n")
    result = ""
    for i in s:
        trimmed = ""
        for j in i:
            if j not in markers:
                trimmed += j
            else:
                break
        trimmed = trimmed.rstrip()
        result = result + trimmed + "\n"
    return result[:-1]


"""Разделитель"""
def solution(string,markers):
    """
    Данное решение с ответов на codewars.com
    и оно не РАБОТАЕТ!!!!
    """
    parts = string.split('\n')
    for s in markers:
        parts = [v.split(s)[0].rstrip() for v in parts]
    return '\n'.join(parts)