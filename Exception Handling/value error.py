try:
    age = float(input("Enter the age :"))
    if age >=18:
        print("you are eligible for vote")
    else :
        raise ValueError
except ValueError:
    print("invalid input")
finally :
    print("age is verified")