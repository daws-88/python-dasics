from optparse import Values


def multi(a,b):
    return a * b
res = multi([1,2,3], 3) ## list repetition
print(res)

def multi(a: int, b: int) -> int:
    return a * b
res = multi([1,2,3], 3) ## list repetition
print(res)


# def mult(a,b):
#     return a * b
# res = mult('3.0',6, a=5,b=4)
# # a=5,b=4 are keyword args as thet contain key and values
# # 3.0 ,6 is postional arg 
# print(res)


def mult(a,b,*args,**kwargs):
    print(f"a:{a},b:{b}, args:{args}, kwargs:{kwargs}") # f - format string , r- raw string
    return a * b
res = mult('3.0',6, 5,4,c=8,d=3)
# a=5,b=4 are keyword args as thet contain key and values
# 3.0 ,6 is postional arg 
# *args - pass any no of postional args
# **kwargs - pass any no of keyword args
## keyword args should be last
print(res)

"""
When we specify data type in function but if we give different data type when passing the values what happen
"""

# def abc(a:int, b:float) -> float:
#     return a + b
# print(abc(1, 2.0))

def calc(a,b,operation):
    if operation == "add":
        return a + b
    if operation == "sub":
        return a - b
    if operation == "mult":
        return a * b

a,b = tuple(map(int,input("enter two values:" ).split()))
operation = input("enter operatio to perforn (add,sub,mult): ")
print(a,b)
res = calc(a, b, operation)
print(res)
