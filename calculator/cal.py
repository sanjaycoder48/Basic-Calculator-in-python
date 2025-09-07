num1 = float(input("Enter the num1: "))
op = input("Enter the operator: ")
num2 = float(input("Enter the num2: "))

if op == "+":
 print(num1 + num2)
elif op == "-":
   print(num1 - num2)
elif op == "*":
   print(num1 * num2)
elif op == "/":
   print(num1 / num2)
else:
   print("Invalid operator")

print("Thank you for using the calculator")
print("Have a nice day")