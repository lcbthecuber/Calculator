def add(num1, num2):
  return num1 + num2

def subtract(num1, num2):
  return num1 - num2

def multiply(num1, num2):
  return num1 * num2

def divide(num1, num2):
  return num1 / num2
  
def run_program():

  print("pick which operations!  1, add, 2, subtract,")
  print(" 3, multiply,  4, divide")

  select = float(input("Select operations from 1, 2, 3, 4 "))
  if select > 4 or select < 1:
    print("This is not avaliable")
    return None
  num1 = float(input("Enter the first number"))
  num2 = float(input("Enter the second number"))


  if select == 1:
    print(num1, "+", num2, "=", add(num1, num2))

  elif select == 2:
    print(num1, "-", num2, "=", subtract(num1, num2))

  elif select == 3:
    print(num1, "*", num2, "=", multiply(num1, num2))

  elif select == 4:
    print(num1, "/", num2, "=", divide(num1, num2))

  else:
    print ("This is not avaible")


run_program()