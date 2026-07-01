bill = float(input("what is bill amount?$"))
tip_percent = float(input("what tip percentage would you like to give? 10, 12, or 15? "))

tip_amount = bill * (tip_percent/ 100)
total = bill + tip_amount

print(f"tip amount: ${tip_amount:.2f}")
print(f"total bill: ${total:.2f}")

split = int(input("how many people are splitting the bill?"))
per_person= total / split

print(f" each person pays: ${per_person:.2f}")