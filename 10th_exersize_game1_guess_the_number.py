#This is a Game 
#Guess the number Game
import random 
print("            This game is present by \'SR\' Gameing \n\n                    \"Guess the number\"\n")
print("\nyou'r guessing number is  under \"0 to 100\" \n")
print("                 \"Your Total life is  (9)\"")
print("")
NUM = random.randint(0,100)
I=0
while(True):
      if(I==9):
             nul = input("\npress any key\n")
             print("\nGame Over Please try again \nThe and is ",NUM)
             break
      print("\nyour life remaing:-",9-I)
      I=I+1
             
      num = int(input("\nEnter Guess Number:- "))
      if(NUM>num):
            print("\nWrong Answer! you answer is less then guess the number \nPlease  Increase your Number")
      if(NUM<num):
             print("Wrong Answer! you answer is Garter  then guess the number \nPlease Decrease you Number")
      if(num == NUM):
            print("\n\n     🎉🎉🎉🎉🎉🎉congratulation!!! you won 🎉🎉🎉🎉🎉🎉")
            break
