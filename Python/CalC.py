a = int(input("Enter the firrst number: "))
b = int(input("Enter the second number: "))

operation = input("chose oeration in these : +, -, *, /, //,** :")

if (operation == "+"):
    print("Addition of these numbers is :", a+b)
elif(operation== "-"):
    print("Substraction of the numbers is : ",a-b)
elif(operation == "*"):
    print("Multiplication of the numbers is : ", a*b)
elif(operation == "/"):
    print("Division of the numbers : ". a/b)
elif(operation== "//"):
    print("floor divison of the numbers :", a//b)
else:
    print("power of the number is :", a**b)

