"""
File withas.py
"""
'''
class TraceBlock:
    def message(self, arg):
        print('running' + arg)
    
    def __enter__(self):
        print('starting with block!')
        return self
    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type is not None:
            print('exited normally\n')
        else:
            print('raise an exception! ' + str(exc_type))

            return False
if __name__ == '__main__':
    with TraceBlock() as action:
        action.message('test 1')
        print('reached')
    with TraceBlock() as action:
        action.message('test 2')
        raise TypeError
        print('not reached')
'''

with open('data') as fin, open('res', 'w') as fout:
    for line in fin:
        if 'some key' in line:
            fout.write(line)
