print("Welcome to the tip calculator.")
total_bill = int(input("what was the total bill?"))
precentage = int(input("What precentage tip would you like to give?10,12, or 15? "))
precent= (precentage/100)+1
who_many = int(input("How many people to split the bill?"))
calculate = round((total_bill/who_many)*precent,0)
each_person = print(f"Each person should pay:{calculate}")