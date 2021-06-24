#PROJECT GUESS[MY FIRST GAME]
import random
print("\t\t\t\t:Welcome to Suryashish's Game Of Random Numbers:")
print('\n')
print('\t\t\t\t\t\t::::MENU::::')
print('Press 1 For Very Easy Level (12 Tries)')
print('Press 2 For Medium Level (8 Tries)')
print('Press 3 For Hard Level (5 Tries)')
print('Press 4 For Extreme Level (3 Tries)')
a=int(input ('Enter Your Desired Level-->'))
print('\t\t\t\t:::CHOOSE THE RANGE:::')
print("Press 'a' for The Range 1-25")
print("Press 'b' for The Range 1-50")
print("Press 'c' for The Range 1-75")
print("Press 'd' for The Range 1-100")
r=input('Enter Your Desired Option-->')
if r=='a' or 'A':
    ra=25
elif r=='b' or 'B':
    ra=50
elif r=='c' or 'C':
    ra=75
elif r=='d' or 'D':
    ra=100
elif r!='a' or r!='b' or r!='c' or r!='d' or r!='A' or r!='B' or r!='C' or r!='D':
    print('Error!Please Follow the Instructions and give the Proper Command..Please Restart the Game')
if a==1:
    b=random.randint(1,ra)
    score=100
    count=0
    for i in range(1,13):
        print('Guess No.:',i)
        c=int(input('Enter Your Guess-->'))
        if c==b:
            print('Congratulations You Have Won This Game!! With A Score Of:',score)
            break
        elif c>b:
            print('You have a got a Bigger Number..Try to Reduce it!!TRY AGAIN!!')
            print('No. of Guesses Left:',12-i)
            score+=100
        elif c<b:
            print('You have a got a Smaller Number..Try to Increase it!!TRY AGAIN!!')
            print('No. of Guesses Left:',12-i)
            score+=100
        count+=1
    if count==12:
        print('Bad Luck!!You Have Lost The Game..Better Luck Next Time')
elif a==2:
    b=random.randint(1,ra)
    score=100
    count=0
    for i in range(1,9):
        print('Guess No.:',i)
        c=int(input('Enter Your Guess-->'))
        if c==b:
            print('Congratulations You Have Won This Game!! With A Score Of:',score)
            break
        elif c>b:
            print('You have a got a Bigger Number..Try to Reduce it!!TRY AGAIN!!')
            print('No. of Guesses Left:',8-i)
            score+=100
        elif c<b:
            print('You have a got a Smaller Number..Try to Increase it!!TRY AGAIN!!')
            print('No. of Guesses Left:',8-i)
            score+=100
        count+=1
    if count==8:
        print('Bad Luck!!You Have Lost The Game..Better Luck Next Time')
elif a==3:
    b=random.randint(1,ra)
    score=100
    count=0
    for i in range(1,6):
        print('Guess No.:',i)
        c=int(input('Enter Your Guess-->'))
        if c==b:
            print('Congratulations You Have Won This Game!! With A Score Of:',score)
            break
        elif c>b:
            print('You have a got a Bigger Number..Try to Reduce it!!TRY AGAIN!!')
            print('No. of Guesses Left:',5-i)
            score+=100
        elif c<b:
            print('You have a got a Smaller Number..Try to Increase it!!TRY AGAIN!!')
            print('No. of Guesses Left:',5-i)
            score+=100
        count+=1
    if count==5:
        print('Bad Luck!!You Have Lost The Game..Better Luck Next Time')
elif a==4:
    b=random.randint(1,ra)
    score=100
    count=0
    for i in range(1,4):
        print('Guess No.:',i)
        c=int(input('Enter Your Guess-->'))
        print('No. of Guesses Left:',3-i)
        if c==b:
            print('Congratulations You Have Won This Game!! With A Score Of:',score)
            break
        elif c>b:
            print('You have a got a Bigger Number..Try to Reduce it!!TRY AGAIN!!')
            print('No. of Guesses Left:',3-i)
            score+=100
        elif c<b:
            print('You have a got a Smaller Number..Try to Increase it!!TRY AGAIN!!')
            print('No. of Guesses Left:',3-i)
            score+=100
        count+=1
    if count==3:
        print('Bad Luck!!You Have Lost The Game..Better Luck Next Time')
elif a!=1 or a!=2 or a!=3 or a!=4:
    print('Error!Please Follow the Instructions and give the Proper Command..Please Restart the Game')
print('\n')
print('\t\t\t\t\t\t\t:::::Thank You For Playing This Game:::::')
print('<-----This Game Was Made By Suryashish Guha----->')


