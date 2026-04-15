
# To calculate the tip percentage based on the total bill amount and the tip amount.

def calculate_tip_percentage(bill_amount, tip_amount):
    if bill_amount <= 0:
        print("Bill amount must be greater than zero.")
    else:
        tip_percentage = (tip_amount / bill_amount) * 100
        return tip_percentage
# Example usage
tip = calculate_tip_percentage(100 , 10) # Should return 20.0
print("The tip amount is : ", tip)