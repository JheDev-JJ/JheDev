print("----------FizzBuzz----------")

# for i <= 100
# printing 1 to 100
for i in range(1, 101):
    # if 6 / 5 = 1 false
    # if 5 / 5 = 0 True and 5 / 25 = .20 False
    if i % 5 == 0 and i % 25 == 0:
        print("FizzBuzz")
    elif i % 5 == 0 :
        print("Fizz")
    elif i % 25 == 0 :
        print("FizzBuzz")
    else:
        print(i)
