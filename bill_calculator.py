"""
Smart Electricity Billing System
--------------------------------
This program calculates the monthly electricity bill
based on slab-wise unit consumption.
"""

def calculate_bill(units: float) -> float:
    """
    Calculate electricity bill based on unit slabs.

    Slabs:
    - Up to 100 units: ₹1.50 per unit
    - 101–300 units: ₹3.00 per unit
    - 301–500 units: ₹5.50 per unit
    - Above 500 units: ₹8.00 per unit
    """
    bill_amount = 0.0

    if units <= 100:
        bill_amount = units * 1.50

    elif units <= 300:
        bill_amount = (100 * 1.50) + (units - 100) * 3.00

    elif units <= 500:
        bill_amount = (100 * 1.50) + (200 * 3.00) + (units - 300) * 5.50

    else:
        bill_amount = (
            (100 * 1.50) +
            (200 * 3.00) +
            (200 * 5.50) +
            (units - 500) * 8.00
        )

    return bill_amount


def main():
    """Main function to take input and display the bill."""
    try:
        units_consumed = float(input("Enter total units consumed: "))

        if units_consumed < 0:
            print("Units consumed cannot be negative.")
            return

        total_bill = calculate_bill(units_consumed)

        print("\n----- Electricity Bill Statement -----")
        print(f"Units Consumed      : {units_consumed}")
        print(f"Total Amount Payable: ₹{total_bill:.2f}")
        print("-------------------------------------")

    except ValueError:
        print("Invalid input! Please enter a numeric value.")


if __name__ == "__main__":
    main()
