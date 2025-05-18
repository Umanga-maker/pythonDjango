# Dictionaries
my = {1: 'Test', 'Name': 'Jim'}
my[3] = 'doit'
my[1] = 'doitfast'
del my[3]
for key,value in my.items():
    print(str(key) + " : " + value)

# args and kwargs
def sum_of(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

print(sum_of(3,6,4,8,9,3))

def sum_of(**kwargs):
    sum = 0
    for k, v in kwargs.items():
        sum += v
    return round(sum, 2)

print(sum_of(coffee=3.65, cake=4.99, juice = 7.38))

# Exceptions
def divide_by(a,b):
    return a / b

try:
    ans = divide_by(3 / 0)

# except Exception as e:
#     print("Something went wrong!", e)
#     print(e.__class__)

except ZeroDivisionError as e:
    print(e, "we cannot divide by zero")
except Exception as e:
    print(e, "something went wrong")
