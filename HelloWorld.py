#Print an introduction
print("Welcome to Python")

def AskQuestion():
    #Ask for input 
    print("Would you like to print Hello World? Y(yes) or N(No)")
    ReadInput()


def ReadInput():
    
    response = input()
    if response == "Y" or response == "N":
        PrintResponse(response)
    else:
        print("Wrong Input. Please type Y or N")
        ReadInput()
       
def PrintResponse(x):
    #Check your status
    if x == "Y":
        print("hello World")
    elif x == "N":
        print ("As you want! Goodbye!")
   
AskQuestion()