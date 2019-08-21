

def mytest(another):
    return another()

def sum():
    return 30 + 59

print(mytest(sum))

mylist = [23,56,21,45,89,26]

print([x for x in mylist if x!= 23])
