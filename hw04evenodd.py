# No need to use if elif else statement because it has only two options
# using choices depends on the scenarios
print("---------- Even Odd Checker ----------")

x = (int(input("Enter a number: ")))
if x % 2 == 1:
    print("Odd Number")
else:
    print("Even Number")