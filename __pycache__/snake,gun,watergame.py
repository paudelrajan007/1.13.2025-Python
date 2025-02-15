# Snake ,Water and Gun Game
import random
'''
 1 for snake
 -1 for water
 0 for gun
 '''
computer = random.choice([-1,0,1])
yourstr = input("Enter your choice : ")
yourDict = {"s":1,"w":-1,"g":0}
reverseDict = {1:"Snake",-1:"Water",0:"Gun"}
you = yourDict[yourstr]

print(f"You chose {reverseDict[you]}\n Computer chose {reverseDict[computer]}")

if (computer==you):
    print("Its a draw")
else:
    if(computer==1 and you == -1):
        print("computer win")
    elif(computer==0 and you==1):
        print("computer win")
    elif(computer==-1 and you==0):
        print("computer win")
    elif(computer==-1 and you==1):
        print("you  win")
    elif(computer==1 and you==0):
        print("you win")
    elif(computer==0 and you==-1):
        print("you win")
    else:
        print("Some things went error'404:' ")
        
