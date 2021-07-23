#ROCK PAPER SCISSOR GAME MADE BY SURYASHISH GUHA
import random
print('\t\t\t\t\t\tRETURN OF ROCHAMBEAU\n')
print('\t\t\t\t\t\t  **INTRUCTIONS**')
print('''*Every Round Consists of 5 Draws.
*You Can Play Any Number Rounds as per your convinience.
*Please Enter The Value as Asked By the Game.
*If You Give any Invalid Input.The Draw Will be cancelled
*You Have to choose Rock,Paper or Scissor.
*Rock Defeats Scissor.
*Scissor Defeats Paper.
*Paper Defeats Rock.
*10 Points will be given if You Win the Round.
*5 Points will be given if the Round is Drawn.
*At the end if your score is Greater than the Computer.YOU WIN!!''')
rounds=int(input('Enter the Number of Rounds you want to play-->'))
userscore=0
compscore=0
rps=['rock','paper','scissor']
for i in range(1,rounds+1):
    print('Round no.:-',i)
    for j in range(1,6):
        print('Draw No.:',j)
        userchoice=input('Please Enter Your Choice Here-->')
        cchoice=random.choice(rps)
        if cchoice==userchoice.lower():
            print('Computer Chose',cchoice)
            print('Ah!Its a Draw.You got 5 points.')
            userscore+=5
            compscore+=5
        elif userchoice.lower()=='rock' and cchoice=='scissor':
            print('Computer Chose',cchoice)
            print('You Won This Draw!!You got 10 points.')
            userscore+=10
        elif userchoice.lower()=='paper' and cchoice=='rock':
            print('Computer Chose',cchoice)
            print('You Won This Draw!!You got 10 points.')
            userscore+=10
        elif userchoice.lower()=='scissor' and cchoice=='paper':
            print('Computer Chose',cchoice)
            print('You Won This Draw!!You got 10 points.')
            userscore+=10
        elif userchoice.lower()=='scissor' and cchoice=='rock':
            print('Computer Chose',cchoice)
            print('You Lost This Draw!!You got No points.')
            compscore+=10
        elif userchoice.lower()=='rock' and cchoice=='paper':
            print('Computer Chose',cchoice)
            print('You Lost This Draw!!You got No points.')
            compscore+=10
        elif userchoice.lower()=='paper' and cchoice=='scissor':
            print('Computer Chose',cchoice)
            print('You Lost This Draw!!You got No points.')
            compscore+=10
        else:
            print('Invalid Input!!This Draw will be cancelled')
    print('Your Score At the End of Round',i,'is:',userscore)
print('Your Final Score is:',userscore)
if userscore>=compscore:
    print('Congratulations!!You Won This Game')
else:
    print('You Lost..Better Luck Next Time!!')
print('''Thank You For Playing This game ..
This Game was made by Suryashish Guha From ACE STUDIOS.
Please Give us Your Feedback at suryashish2005@gmail.com
You Can Also Check out My Site https://suryashish14.github.io/Ace_web_dev/''')
#Temporary End       