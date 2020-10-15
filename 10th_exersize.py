#This is a Game 
#Guess the number Game
print("            This game is present by Ashi Gameing \n\n                    \"Guess the number\"\n")
print("                 \"Your Total life is  (9)\"")
print("")
NUM = 18
I=0
while(True):
      print("\nyour life remaing:-",9-I)
      I=I+1
      if(I==10):
             print("\nGame Over Please try again \nThe and is ",NUM)
             break       
      num = int(input("\nEnter Guess Number:- "))
      if(NUM>num):
            print("\nWrong Answer! you answer is less then guess the number \nPlease  Increase your Number")
      if(NUM<num):
             print("Wrong Answer! you answer is Garter  then guess the number \nPlease Decrease you Number")
      if(num == NUM):
            print("\n🎉🎉🎉🎉congratulation! you won 🎉🎉🎉🎉")
            break
