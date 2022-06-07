"""
"""

class Wrapper:
    
    def __init__(self, object):
        self.wrapper = object
    
    def __getattr__(self, attrname):
        print('Trace: ' + attrname)
        return getattr(self.wrapper, attrname)
