# Inputs we need from user
# 1. Monthly Rent
# 2. Fooding Expenses
#  3. Electricity Bill
# 4. Charge per unit of electricity
# 5. Water Bill
# 6. Internet Bill
# 7. Number of Persons are living

# Get user inputs
monthly_rent = float(input("Enter your monthly rent: "))
food_expenses = float(input("Enter your monthly food expenses: "))
electricity_bill = float(input("Enter your monthly electricity bill: "))
water_bill = float(input("Enter your monthly water bill: "))
internet_bill = float(input("Enter your monthly internet bill: "))
persons = int(input("Enter number of persons living: "))

# Calculate total expenses
total_expenses = (monthly_rent + food_expenses + electricity_bill + water_bill + internet_bill) / persons
expenses = monthly_rent + food_expenses + electricity_bill + water_bill + internet_bill
# Display the result
print("Total expenses: ", expenses)

print("Total expenses per person: ", total_expenses)