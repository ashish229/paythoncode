#Exersize
#Guess the number Game

NUM = 18
I=0
while(True):
      print("\nyour Guesses rimneder:-",9-I)
      I=I+1
      if(I==10):
             break       
      num = int(input("Enter Guess Number:- "))
      if(NUM>num):
            print("Increase your Number")
      if(NUM<num):
             print("Decrease you Number")
      if(num == NUM):
            print("\ncongratulation you Guess the Number")
            break
print("\nGame Over")
