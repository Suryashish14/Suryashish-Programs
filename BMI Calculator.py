#BMI Calculator
print( '\t\t\t\t\t\t\t\tBMI Calculator')
a=input('Write Your Name-->')

b=float(input('Enter Your Weight(in KiloGram)-->'))
c=float(input('Enter Your Height(in Metre)-->'))
BMI=b /(c*c)
print('Your BMI Is:',BMI)
if BMI <= 18.5:
    print(a,'is Underweight')
elif BMI > 18.6 and BMI < 24.9:
    print(a,'is Perfect')
elif BMI > 25.0 and BMI < 29.9:
    print(a,'is Overweight')
else :
    print(a,'is Obese')
