a = [1,2,3,4,5]
b = [1,2,3,4,5]
c = a

# # Comparing and printing return values
print(a is c)
print(a is b)

# # printing IDs of a, b and c
print("id(a) :", id(a))
print("id(b) :", id(b))
print("id(c) :", id(c))


########
a = 'umanga'
b = 'umanga'
print(a is b)
print("id(a) :", id(a))
print("id(b) :", id(b))