
def outer_parlor():
    ice_cream = "Vanilla"

    def inner_scoop():
        ice_cream = "Strawberry"
        print("Inside the inner scoop (Local):", ice_cream)

    inner_scoop()
    print("Inside the outer parlor (Enclosing):", ice_cream)


outer_parlor()


def outer_func():
    msg = 'Hello there!'
    res = ''

    def inner_func():
        nonlocal res
        res = 'How are you?'
        print(msg)
    inner_func()
    print(res)


outer_func()

my_var = 100


def show_var():
    print(my_var)


show_var()
print(my_var)
my_var_1 = 7


def show_vars():
    global my_var_2
    my_var_2 = 10
    print(my_var_1)
    print(my_var_2)


show_vars()

my_var = 10


def change_var():
    global my_var
    my_var = 20


change_var()
print(my_var)
