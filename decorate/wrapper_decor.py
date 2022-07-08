"""
wraper_decor.py file!
"""
class Wrapper:
    def __init__(self, object):
        self.wrapped = object
    
    def __getattr__(self, attrname):
        print(f'Trace: {attrname}')
        return getattr(self.wrapped, attrname)
