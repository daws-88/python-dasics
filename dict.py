d_1 = {}
d_2 = dict()
sample = {'a': 1, 'b': 3}
print(type(sample), sample)
print(sample['a'],sample.get('b'))

# dictonary is a mutable data type also kmown as hasmaps
sample['a'] = 15
print(sample)

Example = {("a", "b"):2, "c": 3}
print(Example)
# keys in dictionaries can not be changed
# keys are immutable ,values are mutable data types
# print(dir(sample))
"""
['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
"""
print(sample.keys(), sample.values(), sample.items())

sample_list = [(('a','b'),1), ('b','2')]
sample_dict = dict(sample_list)
print(sample_dict)