import numpy as np
list1 = [[1,2,3],[4,5,6]]
arr1 = np.array(list1)

print(arr1)

print(list1[0][0])
list1[0][0] += 1
print(list1[0][0])
print(arr1[0][0])
print(list1)
print(arr1)

def m1(list: list):
    #list = np.array(list)
    print("inside m1")
    print(list)
    print("adding 1")
    list[0][0] += 1
    print(list)


m1(list1)
print("outside m1")
print(list1)
print("_________")
dict1 = {"one": "won", "two": "too"}
print(dict1["one"])
print(list(dict1.values())[0])

#print("_______")
#[print(value) for value in dict1.values()]
