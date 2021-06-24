from googlesearch import search
task=input('Enter Your Search-->')
for i in search(task,tld='com',num=10,stop=10,pause=2):
    print(i)
