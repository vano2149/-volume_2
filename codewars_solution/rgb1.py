"""Разделитель"""
def limit(num):
    if num < 0:
        return 0
    if num > 255:
        return 255
    return num


def rgb(r, g, b):
    return "{:02X}{:02X}{:02X}".format(limit(r), limit(g), limit(b))

"""Разделитель"""
def rgb(*args):
    return ''.join(map(lambda x: '{:02X}'.format(min(max(0, x), 255)), args))

"""Разделитель"""
def rgb(r, g, b):
    return '{0:02X}{1:02X}{2:02X}'.format(max(min(r, 255), 0), max(min(g, 255), 0), max(min(b, 255), 0))



"""Разделитель"""
def check(n):
    if n<0: return 0
    if n>255: return 255
    
    return n

def rgb(r, g, b):
    r = check(r)
    g = check(g)
    b = check(b)
    
    hex_val = "%02x%02x%02x" % (r, g, b)

    return hex_val.upper()