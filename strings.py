sample = "Hello, how are you" # or 'Hello'
sample_1 = "xyz" # ("x", "y", "z") 
# python stores strings in the form of tuple so strings are immutable
print(sample[0])

# sample[0] = 'h'
# print(sample[0])

# print(dir(sample))
"""
['capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
"""
print(sample.capitalize()) #Only the first character of the entire string is uppercase.
print(sample.casefold()) # all become lowecase
print(sample.title()) # irst character of every word is uppercase.

text = "Python"
print(text.center(20, "*"))

## reverse a string
print(sample[::-1])
print(tuple(sample_1),list(sample_1))

# split 
sample = "Hello, how are you"
print(sample.split(" "))
print("#".join(sample.split(" ")))

## concating means add two strings
print("a" + "b")

# print copy filepath
print(r"C:\devops\daws-86s\repos\python-dasics\strings.py")