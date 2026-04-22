
try:

    num1 = int(input("Enter the numerator : "))

    num2 = int(input("Enter the denomiator : "))

    result = num1 / num2

    print("The result is : ",result)

except ZeroDivisionError:

    print("Dividing number by zeo is not possible")

except ValueError:

    print("Invalid Input")

finally:

    print("Inputs are validated")