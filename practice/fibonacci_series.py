# Through Recursion

# def fibonacci(i):
#     if i == 0:
#         return 0
#     elif i == 1:
#         return 1
#     else:
#         return fibonacci(i-2) + fibonacci(i-1)
    
# for x in range(13):
#         print(fibonacci(x))


# Without Recursion, using loop

# lst = [0,1]

# n = int(input("enter the no for calculating fib at that position"))

# for i in range(2, n):
#     lst.append(lst[i-1] + lst[i-2])

# print(n,"th position fib no is",lst[n-1])

# print(lst)

fibonacci_cache = {}

def fibonacci(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    if n == 0:
        value = 0
    elif n == 1:
        value = 1
    else:
        value = fibonacci(n-1) + fibonacci(n-2)
    fibonacci_cache[n] = value
    return value

for x in range(13):
    print(fibonacci(x))

