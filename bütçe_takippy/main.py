def get_amount(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Amount cannot be negative!")
                continue
            return value
        except ValueError:
            print("please enter a valid number!")


income = get_amount("Please enter the income: ")
rent = get_amount("Please enter the rent:")
food = get_amount("how much money do you spend on food: ")
transport = get_amount("how much money do you spend on transport: ")
other = get_amount("Please enter your other expenses:")

total_expenses = rent + food + transport + other
remaining_money = income - total_expenses
spending_rate = (total_expenses / income ) * 100 if income > 0 else 0
separator = "-"*40
print(separator)

print(f"your income :{income:.2f} TL\nyour total expenses :{total_expenses:.2f}TL\nyour remaning money : {remaining_money:.2f} TL\nyour speading rate : %{spending_rate:.2f} ")


if income > total_expenses:
    print("You are saving!")
elif income < total_expenses:
    print("You have a debt!")
else:
    print("You neither save money nor have any debt.")

print(separator)    