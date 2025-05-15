def calculate_tax(bill, tax_rate):
    return round((bill * tax_rate) / 100.00 , 2)

print('Total Tax:', calculate_tax(175.00, 15))
print('Total Tax:', calculate_tax(195.45, 19))


#global scope
my_global = 10

def fn1():
    enclosed_v = 8
    
    def fn2():
        local_v = 5
        print('Access to Global', my_global)
        print('Access to enclosed', enclosed_v)
    fn2()

fn1()


#Lists
list1 = [1, 2, 3, 4, 5]
print(list1[3]) # index of list always starts from 0 and 1 , 2 and so on.
list1.extend ([6, 7, 8, 9])
print(list1, sep= " ")

list2 = ['A', 'B', 'C']
print(*list2)
del list2[1] #deletes index number 1
print(list2, sep= " ")

list3 = ['Hello', 1, True, 40.22] # any type
list3.insert(len(list3), False)
print(list3, sep=" ")

list4 = [1, [2,3,4], 5, 6] # nested lists
list4.append(7)# adds the value in the list
list4.pop(3) # deletes the index number 3
print(list4, sep=" ")


# Iteration
list5 = [2, 4, 6, 8]
print(list5, sep= " ")
for x in list5:
    print('Value:', x)



