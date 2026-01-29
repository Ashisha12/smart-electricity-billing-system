def calculate_bill(units):
    if units <= 100:
        amount = units * 1.5
    elif units <= 200:
        amount = 100 * 1.5 + (units - 100) * 2.5
    elif units <= 300:
        amount = 100 * 1.5 + 100 * 2.5 + (units - 200) * 4
    else:
        amount = 100 * 1.5 + 100 * 2.5 + 100 * 4 + (units - 300) * 5
    return amount


try:
    units = int(input("Enter electricity units consumed: "))
    bill = calculate_bill(units)
    print(f"Total Electricity Bill: ₹{bill}")
    print("Thank you for using Smart Electricity Billing System")
except ValueError:
    print("Please enter a valid number.")