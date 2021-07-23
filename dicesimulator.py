import random
print('\t\t\t\t****WELCOME TO DICE SIMULATOR****')
again='y'
while again.lower()=='y':   
    ranchoice=random.randint(1,6)
    print('Here is Your Result:',ranchoice)
    again=input('Type y to continue or anything else to quit: ')
print('''\n**Thank You For Playing Dice Simulator**
This Game was made by Suryashish Guha From ACE STUDIOS.
Please Give us Your Feedback at suryashish2005@gmail.com
You Can Also Check out My Site https://suryashish14.github.io/Ace_web_dev/''')
#Program Terminated Till Further Update.