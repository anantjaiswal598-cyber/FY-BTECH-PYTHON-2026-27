# Input three numbers
a = int(input("Enter the number 'a' = "))
b = int(input("Enter the number 'b' = "))
c = int(input("Enter the number 'c' = "))

# Determine the largest number
if a > b and a > c:
    print("a is the largest")
elif b > c:
    print("b is the largest")
else:
    print("c is the largest")