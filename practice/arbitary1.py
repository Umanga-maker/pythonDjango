# *args = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
# ' * ' unpacking operator allows you to extract elements from data structures

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1, 2, 3, 6, 7, 9))

def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Dr.", "Spongebob", "Harold", "Squarepants", "III")

# *args = parameter that will pack all arguments into a tuple useful so that a function can accept a varying amount of arguments

def add(*stuff):
    sum = 0
    stuff = list(stuff)
    stuff[0] = 0
    for i in stuff:
        sum += i
    return sum

print(add(1,2,3,4,5,6))


# **kwargs returns dictionaries type

def person(name, **data):
    print(name)
    for i, j in data.items():
        print(i,j)

person('Umanga', age=22, city='Kathmandu', mob=9827074266)


def add(*args):
    print(args)
    print(type(args))
    sum = 0
    for i in args:
        sum += i
        print(sum)

add(2,4,6,8,3,6,8)


def my_random_django_view(requests, **kwargs):
    print(kwargs)
    # Product.objects.get(id=kwargs.get('id'))

#path('my-product/:id')
my_random_django_view("requests", id='some_id')

def my_func( *args, **kwargs):
    print("hello world", args, kwargs)

my_func("abc", abc=123)














