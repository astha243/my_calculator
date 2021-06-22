def add(num1, num2):
    result = num1 + num2
    print (result)
    return result
def sub(num3, num4):
    result = num3 - num4
    print(result)
    return result
def mul(num5, num6):
    result = num5 * num6
    print(result)
    return result    
def truediv(num7, num8):
    result = num7 / num8
    print(round(result))
    return result

while True:
    print ("Options: ")
    print ("Sum of two numbers?\n enter + ")
    print ("Difference of two numbers?\n enter -")
    print ("multiplication of two numbers?\n enter *")
    print ("Division of two numbers?\n enter /")
    print ("Want out?\n enter quit ")
    user_input = input(": ")


    if user_input == "quit":
        print("calculator at rest")
        break
    elif user_input == "+":
        num1 =int(input("Enter your fist number: "))
        num2 = int(input("Enter your second number: "))
        add(num1, num2)
    elif user_input == "-":
        num3 = int(input("Enter your fist number: "))
        num4=  input(("Enter your second number: "))
        sub(num3, num4)
    elif user_input == "*":
        num5 = int(input("Enter your fist number: "))
        num6 = int(input("Enter your second number: "))
        mul(num5, num6)
    elif user_input == "/":
        num7 = int(input("Enter your fist number: "))
        num8 = int(input("Enter your second number: "))
        truediv(num7, num8)