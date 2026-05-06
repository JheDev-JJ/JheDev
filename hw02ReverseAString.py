# getting the word starting from index 0
# 0=H 1=E 2=L 3=L 4=O
print("Hello World"[4])

#getting the word backward starting from the right
# -1=d -2=l -3=r -4=o
print("Hello World"[-4])

#getting the word straight from index 0 then it will stop when it reach the index number
# When negative it will deduct the index from right to left and stop at the index number
# Example
# [:2] It will give 0=H 1=E 2=L 
# it will not print the 2 because its stop
print("Hello World"[:-2])


# positive is still the same but if example is ::2 it will jump each index by 1 but starting at index 0
# example of positive ::2 HloWrd
# This is the reverse string works if its ::-1 it will reverse the word
print("Hello World"[::-1])





