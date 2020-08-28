number =int(input('\nEnter a number >> '))
def PrimeCheck():
    flag = 0
    if number > 1:
        for i in range(2, number//2+1):
            if number % i == 0:
                flag += 1
                break

    if flag == 0 and number != 1:
        if number <= 0:
            ans='Is invalid input! Please Give Any Positive Value'
            return ans
        else:
             ans='is prime'
             return ans
    elif flag == 1:
        ans='is not prime'
        return ans
    elif number == 1:
         ans=' is neither prime nor composite'
         return ans
print(number,PrimeCheck())