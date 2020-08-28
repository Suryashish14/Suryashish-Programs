def Hello():
   a=int(input('Enter a Number:'))
   print(a,number+1)
arr = []
add = 0
elements = int(input("Enter the number of elements in the list >> "))
numcopy=elements
for number in range(elements):
    print("Enter number ", number+1)
    arr.append(int(input()))
for i in arr:
    add += i
print('\nThe Sum Of The Terms Is:',add)
print('The Average Of The Terms Is:',add/numcopy)