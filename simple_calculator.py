# Function definition for the math operations.

def add(num1,num2):
    print(num1+num2)
def sub(num1,num2):
    print(num1-num2)
def mult(num1,num2):
    print(num1*num2)
def div(num1,num2):
  try:
      print(num1/num2)
  except ZeroDivisionError as err:
      print(err)

# Defining a boolean exit button.
leave = False
# while loop in function to our boolean button
while leave == False :
    # Getting input from the user.

    num1 = float(input("First number: "))
    oper= input("Operation: ")
    num2 = float(input("Second number: "))

    #conditionals for the final result.

    if oper == "add" or oper == "+" or oper == "sum":
      add(num1, num2)
    elif oper == "subtraction" or oper == "-":
      sub(num1,num2)
    elif oper == "multiplication" or oper == "multiply"or oper == "x" or oper =="*":
      mult(num1,num2)
    elif oper=="division" or oper=="div" or oper=="divide" or oper=="/":
      div(num1,num2)
    else:
      print("Invalid operator, please try again!")

    # Getting input about user wanting to quit the app.
    question = input("Do you wish to exit? Y/N ")
    if question == "Y" or question =="y":
        leave = True
    elif question == "N" or question == "n":
        leave = False
    else:
        print("Invalid answer, leaving...")
        leave = True



