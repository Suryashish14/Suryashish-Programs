import time
import random
t=0
txt='Hello my name is Suryashish'
print('Type this sentence....')
print(txt)
start_time=time.time()
user=input('\n>> ')
end_time=time.time()
time_elapsed=int(end_time-start_time)
if time_elapsed==0:
    t=1
else:
    t=time_elapsed
correct=0
error=0
for i,j in zip(txt,user):
    if i==j:
        correct+=1
    else:
        error+=1

# (correct characters)x100/ (total characters in sentence)<---Accurancy
accuracy=(correct*100)/len(txt)
words=user.split()
wpm=len(words)//(t/60)
print('You took',t,'seconds')
print('Your Typing speed is',wpm,'wpm')
print('You have an accuracy of',accuracy,'%')