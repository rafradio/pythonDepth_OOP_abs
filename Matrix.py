import abc
from collections.abc import MutableMapping

class BaseDict(MutableMapping, metaclass=abc.ABCMeta):
        def __init__(self, *args, **kwds):
            self.store = {}
            self.rows = kwds['rows']
            self.columns = kwds['columns']
            for el in args[0]:
                mapping = {(el[0], el[1]): el[2]}
                self.store.update(mapping)
            # print("hello ", self.store)

        def __getitem__(self, key):
            return self.store[key]
        
        def __setitem__(self, key, value):
            self.store[key] = value

        def __delitem__(self, key):
            del self.store[key]

        def __len__(self):
            return len(self.store)
        
        def __iter__(self):
            return iter(self.store)
        
        def __str__(self):
            txt = str()
            for i in range(self.rows):
                txt += ' '.join([f'{str(self.store[i+1, j+1])}  ' for j in range(self.columns)]) + '\n'
            return txt
        
        def __repr__(self):
            return repr(self.store)
        
        @abc.abstractmethod
        def __mul__(self):...

        @abc.abstractmethod
        def __add__(self):...
