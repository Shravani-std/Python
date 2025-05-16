def add(x,y):
    return x+y

def subtract(x,y):
    return x - y

def multiply(x,y):
    if x == 0 or y == 0:
        return 0
    return x*y

def divide(x,y):
    if y == 0:
        return "Error"
    return x/y


def main():

    print("Calculator")
    print("Select Operation: " \
    "\n1. Addition" \
    "\n2. Subtraction" \
    "\n3. Multiplication" \
    "\n4. Division")


    while True:
        opr = input("Enter Operation number u want to perform (1-4): ")
        if opr not in ["1","2","3","4"]:
            print("Invalid number ")
        else:
            break

    try:
        x = float(input("Enter first number "))
        y = float(input("\nEnter second number "))
    except ValueError:
        print("Error! Enter valid number ")
        


    if opr == "1":
        print(f"Addition of {x} and {y} is: {add(x,y)}")
    elif opr == "2":
        print(f"Subtraction of {x} and {y} is: {subtract(x,y)}")
           
    elif opr == "3":
        print(f"Multiplication of {x} and {y} is: {multiply(x,y)} ")
            
    elif opr == "4":
        print(f"Division of {x} and {y} is: {divide(x,y)}")
    else:
        print("Invalid choice")

    again = input("Do you want to perform another operation? (y/n) ")

    if not again.startswith("y"):
        print("Thank you!")
        return
    else:
        main()

main()
