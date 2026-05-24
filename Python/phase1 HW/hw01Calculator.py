print("------------------------------------------")
print("          Building A Calculator           ")
print("------------------------------------------")
print("Choosing the following are : (+)  (-) , (*) , (/) ")

choose = input("Type of Operators : ")
num1 = float((input("Enter a num1: ")))
num2 = float((input("Enter a num2: ")))

if(choose == '+'):
    result = num1 + num2
elif (choose == '-'):
    result = num1 - num2
elif (choose == '*'):
    result = num1 * num2
elif (choose == '/'):
    result = float(f"{num1:.2f}") / float(f"{num2:.2f}")

print(f"Result: {result:.2f}")


