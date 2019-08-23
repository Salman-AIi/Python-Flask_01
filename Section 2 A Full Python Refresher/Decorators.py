import functools

def my_decor(func):
    @functools.wraps(func)
    def function_that_runs_stuff():
        print('Hi noob')
        func()
        print('Hi pro')
    return function_that_runs_stuff

@my_decor
def homie():
    print('HOMIE')


#homie()
import functools
def decorator_with_arguments(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_runs_func(*args,**kwargs):
            print('in decorator')
            if number == 56:
                print('NOT RAN')
            else:
                func(*args,**kwargs)
            print('after decorator')
        return function_that_runs_func
    return my_decorator

@decorator_with_arguments(56)
def running_noob(number):
    print('RAN')

running_noob(3)
