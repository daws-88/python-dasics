t1 = ()
t2 = tuple()
sample = ("172.32.12.45", "12.32.45.4", True, "ansible", 12, 3.14)
print(type(sample))
print(sample[2])

## tuple is a immutable data type
# sample[1] = "123"
# print(sample) # we gget error

slice = sample[0:3]
print(slice)
slice_1 = sample[-1]
print(slice_1)

# print(dir(sample))
"""
1. count
2. index
"""
Example =(1, 4, 7, 3, 4, 2)
print(len(Example))
print(Example.count(4))
print(Example.index(2))

## type casting means :: data type conversion
sample = ("172.32.12.45", "12.32.45.4", True, "ansible", 12, 3.14)
sample_1 = list(sample)
print(type(sample_1), sample_1)

sample_t = tuple(sample_1)
print(type(sample_t), sample_t)