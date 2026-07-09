def calc(x):
    return x * 2
num = [2,4.0]
res = list(map(int,map(calc,num)))
print(res)