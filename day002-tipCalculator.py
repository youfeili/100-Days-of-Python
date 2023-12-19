# Greeting
print("Welcome to the tip calculator.")

# Ask for total bill
total = float(input("What was the total bill? $"))

# Ask for percentage
percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

# Ask how many people are spliting the bill
people = int(input("How many people to split the bill? "))

# Calculate pay per person
total_after_tip = total * (1 + percent / 100)
pay_per_person = total_after_tip / people

# Display how much each person should pay
print(f"Each person should pay: ${round(pay_per_person, 2)}")