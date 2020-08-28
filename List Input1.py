arr = []
add = 0
elements = int(input("Enter the number of elements in the list >> "))
numcopy=elements
for number in range(elements):
    a=int(input("Enter number %i >> "%(number+1)))
    arr.append(a)
for i in arr:
    add += i
print('\nThe Sum Of The Terms Is:',add)
print('The Average Of The Terms Is:',add/numcopy)