def greet_me(**kwargs):  # kwargs - keyword arguments
    print('Result from kwang function Greet_me')
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))


def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)


#Code:


greet_me(name1='test1', name2= 'test2', testcase = '1',dic = {"dic1":'word1'} ) # You will have to specific keyword for the arg that you send to the class
test_var_args('yasoob', 'python', 'eggs', 'test') #so for *argv does not have to specific name

kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
greet_me(**kwargs)

