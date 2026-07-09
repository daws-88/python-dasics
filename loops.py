## while loop ## 
# in while loop we  must specify condition

# a = 0
# while a <= 10:
#     if a == 6:
#         a = a + 1
#         continue
#         # break
#     print(a)
#     a = a + 1

sample = ["server1", "server2", "server3", "server4"]
idx = 0
while idx < len(sample):
    print(sample[idx])
    idx = idx + 1


## for loop
# in - membership operator - checks element is present or not
print("server1" in sample)

for idx in sample:
    print(idx)


# access elements inside a list with index using for loop
# range, enumerate
print(list(range(5)))

for i in range(len(sample)):
    print(sample[i])

print(enumerate(sample))

for  val in enumerate(sample):
    print(val)

for ene, val in enumerate(sample):
    print(ene, val)
    
# tuple unpacking
x , y = (4, 6)
print(x ,y)

# while loop can be used when we know when to end
# for loop can be be when we don't know when to end