"""
Mapattrs.py file!
"""
import pprint

def trace(X, label = '', end='\n'):
    print(label + pprint.pformat(X) + end)

def filterdictvals(D,V):
    """
    Словарь D c элементами после удаления значения V.
    """
    return {K: V2 for (K, V2) in D.items() if V2 != V}

def invertdict(D):
    """
    """
    def keysof(V):
        return sorted(K for K in D.keys() if D[K] == V )
    return {V : keysof(V) for V in set(D.values())}

def dflr(cls):
    """
    Реализация классического порядка!
    """
    here = [cls]
    for sup in cls.__bases__:
        here += dflr(sup)
    return here

def inheritance(instance):
    """
    Порядок поиска при наследовании:
        нового стиля (MRO)
        класического (DFLR)
    """
    if hasattr(instance.__class__, '__mro__'):
        return (instance,) + instance.__class__.__mro__
    else:
        return [instance] + dflr(instance.__class__)

def mapattrs(instance, withobject = False, bysource =False):
    """
    Словарь с ключами делающий атрибуты экземплярами.
    """
    attr2obj = {}
    inherits = inheritance(instance)
    for attr in dir(instance):
        for obj in inherits:
            if hasattr(obj, '__dict__') and attr in obj.__dict__:
                attr2obj[attr] = obj
                break
    if not withobject:
        attr2obj = filterdictvals(attr2obj, object)
    return attr2obj if not bysource else invertdict(attr2obj)

if __name__ == '__main__':
    print('Classic classes in 2.x, new-style in 3.x')

    class A: attr1 = 1
    class B(A): attr2 = 2
    class C(A): attr1 = 3
    class D(B, C): pass

    I= D()
    print(f"Py => {I.attr1}")
    trace(inheritance(I), 'INH\n')
    trace(mapattrs(I), 'ARRTS\n')
    trace(mapattrs(I, bysource=True), 'OBJS\n')
    print('New-style classes in 2.x and 3.x')
    class A: attr1 = 1

    class B(A): attr2 = 2
    class C(A): attr1 = 3
    class D(B, C): pass
    I = D()
    print(f'Py => {I.attr1}')
    trace(inheritance(I), 'INH\n')
    trace(mapattrs(I), 'ATTRS\n')
    trace(mapattrs(I, bysource=True), 'OBJS\n')
