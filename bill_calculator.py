def calculate_bill(units):
    total_bill = 0
    
    if units <= 100:
        total_bill = units * 1.50  # Rural/Low usage rate
    elif units <= 300:
        total_bill = (100 * 1.50) + (units - 100) * 3.00
    elif units <= 500:
        total_bill = (100 * 1.50) + (200 * 3.00) + (units - 300) * 5.50
    else:
        total_bill = (100 * 1.50) + (200 * 3.00) + (200 * 5.50) + (units - 500) * 8.00
        
    return total_bill

# User Input
try:
    user_units = float(input("Enter total units consumed: "))
    amount = calculate_bill(user_units)
    print(f"--- Electricity Statement ---")
    print(f"Units Consumed: {user_units}")
    print(f"Total Amount Payable: ₹{amount:.2f}")
except ValueError:
    print("Please enter a valid number for units.")
