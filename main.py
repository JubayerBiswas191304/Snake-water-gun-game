'''
1 for snake
-1 for water
0 for gun
'''
import random
computer=random.choice([1, -1, 0])
youstr=input("Enter  your choice: ").lower()
you_dict={"s":1,"w":-1,"g":0}
reversed_dict={1:"Snake",-1:"Water",0:"Gun"}
you=you_dict[youstr]
# After that we have 2 character(veriable):you and computer

print(f"You choice {reversed_dict[you]}\nComputer chose {reversed_dict[computer]}")

if(you==computer):
    print("Its a Draw")
else:   
    if(computer==-1 and you==1):
        print("You win")
    elif(computer==0 and you==-1):
        print("You win")
    elif(computer==1 and you==0):
        print("You win")
    elif(computer==1 and you==-1):
        print("You lose")
    elif(computer==0 and you==1):
        print("You lose")
    elif(computer==-1 and you==-0):
        print("You lose")
    else:
        print("something wrong")