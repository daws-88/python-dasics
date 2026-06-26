server_1 = "172.32.12.45"
server_2 = "12.32.45.4"
servers = ["172.32.12.45", "12.32.45.4", True, "ansible", 12, 3.14]
print(server_1, server_2,servers)
server_2 = servers[1]
print("server 2 IP is:", server_2)

## slice fun 
simple_slice = servers[0:3]
print(simple_slice)

## step size 
simple_size =servers[0:6:2]
print(simple_size)

simple_size =servers[1:6:2]
print(simple_size) ## 1 , 1+2, 3+2 ..

## negative indexing
simple_slice = servers[-1]
print("Last value is:", simple_slice)

simple_back = servers[-1:-4:-1]
print(simple_back)

print("Length of list:", len(simple_back))


## List is a mutable data type
## MUTABLE: once we define ,we can change at any time EX: listt ,dict,set
## IMMUTABLE once we define ,we can mot  change at any time EX : tuple 

print("before modification:", servers)
servers[-2] = 9652 ## inplace operation
print("after modification:", servers)

# print("List of operations:", dir(servers))

"""
1. append
"""

servers.append(False)
print(servers)

servers.append(["a","b","c"])
print(servers, len(servers))

# multi indexing or multi slicing
servers[-1][0]
print(servers[-1][0])

servers.extend(["x","y","z"])
print(servers, len(servers))

print(servers.index(True))

servers.insert(0, "python")
print(servers)

servers.remove(True)
print(servers)
