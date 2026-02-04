import math

while True:
    print("\n******* ********* Hammad's Scientific Calculator(Basic Operations) ******* *********")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Logarithm (base 10)")
    print("8. Sine")
    print("9. Cosine")
    print("10. Tangent")
    print("11. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 11:
        print("*******************Calculator Closed********************")
        break

    elif choice in [1, 2, 3, 4, 5]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == 1:
            print("Result:", a + b)
        elif choice == 2:
            print("Result:", a - b)
        elif choice == 3:
            print("Result:", a * b)
        elif choice == 4:
            if b != 0:
                print("Result:", a / b)
            else:
                print("Error! Division by zero")
        elif choice == 5:
            print("Result:", a ** b)

    elif choice == 6:
        num = float(input("Enter number: "))
        if num >= 0:
            print("Result:", math.sqrt(num))
        else:
            print("Error! Negative number")

    elif choice == 7:
        num = float(input("Enter number: "))
        if num > 0:
            print("Result:", math.log10(num))
        else:
            print("Error! Log undefined")

    elif choice == 8:
        angle = float(input("Enter angle in degrees: "))
        print("Result:", math.sin(math.radians(angle)))

    elif choice == 9:
        angle = float(input("Enter angle in degrees: "))
        print("Result:", math.cos(math.radians(angle)))

    elif choice == 10:
        angle = float(input("Enter angle in degrees: "))
        print("Result:", math.tan(math.radians(angle)))

    else:
        print("*****************Invalid Choice******************")