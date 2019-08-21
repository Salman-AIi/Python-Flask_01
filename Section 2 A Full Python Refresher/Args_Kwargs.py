





def ez_addition(*args):
    return sum(args)


def mykwargs (*args ,**kwargs):
    print(args)
    print(kwargs)

mykwargs(4,5,23 , name = 'Jose', Location = 'Homie')

homes = ez_addition(2,5,6,7,8,2,3,4,5)
print(homes)
