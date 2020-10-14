#This program is a calculator 
print("This program is  caluclater of the Two numbers ")
def total(): #user difine function 
      
      c = 0
      
      while (True):
                 
      
            b = int(input("\nEnter the number \n"))
            c = int(input("Enter the number \n"))
            z = input("\nAddition then Enter :       +\nSubtrecation then Enter :   - \nMultiplaction then Enter :  *\ndivision then Enter :.      /\n")
            if("+"==z):
                  d = sum((c,b))#Builed in function ()
                             
            elif("-"==z):
                  d = b-c
            elif("*"==z):
                  d = b*c
            elif("/"==z):
                  d = b/c
            print("\nThe Answer is :- ",d) 
            x = input("\n\nyou are Exit the this calculator  so please Enter \n\"yes\"\n and not exit then Enter \n\"not\"\n\n") 
            if("yes" == x):
                  break
            elif("not" == x):
                  continue
            else:
                  print("\nplease Enter the vailed Condition ")
                  break      
total()
