def triangle():
    a = int(input("Enter first side: "))
    b = int(input("Enter second side: "))
    c = int(input("Enter third side: "))

    # Check triangle inequality theorem
    if a + b <= c or a + c <= b or b + c <= a:
        print("Triangle cannot be formed")
    # Check Pythagorean theorem for right-angled triangle
    elif (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
        print("Triangle is right angled")
    else:
        print("Triangle is not right angled triangle")

# Call the function
triangle()
