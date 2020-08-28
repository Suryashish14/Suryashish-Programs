lower=int(input('Enter The Lower Limit of The Range (Must Be >= 2)-->'))
upper=int(input('Enter The Upper Limit Of The Range--->'))
if lower>=2:
    for number in range(lower,upper+1):
        if number >1:
            for i in range(2,number):
                if number % i == 0:
                    break
            else:
                print(number)
else:
    print('Invalid Input!Lower Limit Should Be Greater Than 2..')    