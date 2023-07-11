from collections.abc import MutableMapping

class BaseDict(MutableMapping):
        def __init__(self, *args, **kwds):
            self.store = {}
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
        
        def __repr__(self):
            return repr(self.store)

# d = BaseDict([(1, 2, 10), (1, 3, 20)])
# # d.update({(1,5): 30})
# m = iter(d)
# print(d)
# print(d[next(m)])
# print(next(m))