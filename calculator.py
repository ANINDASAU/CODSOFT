print("......Here is YOUR SIMPLE CALCULATOR......")

num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))

print("Which operation you want to perform...\n")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("\n")
temp = input("Enter any one operation (1/2/3/4) you want to perform: ")

if temp == '1':
    print("Your choice is for ADDITION--")
    print("The result is: \n",num1 + num2)
elif temp == '2':
    print("Your choice is for SUBSTRACTION--")
    print("The result is: \n",num1 - num2)
elif temp == '3':
    print("Your choice is for MULTIPLICATION--")
    print("The result is: \n",num1 * num2)
elif temp == '4':
    print("Your choice is for DIVISION--")
    if num2!= 0:
        print("The result is: \n",num1/num2)
    else:
        print("Error! divisible by zero not possible")
else:
    print("Your choice is invalid! Please choose either 1 or 2 or 3 or 4\n")

print("Thank you!")  