
bill = float(input("What was your total bill? $"))

#print(bill)

tip_percentage = float(input("How much of a tip would you like to leave? %")) / 100

tip_in_dollars = bill * tip_percentage

#%print(tip)

num_people_splitting = int(input("How many people are splitting the bill? "))

#print(total_tip)

payment_per_person = (tip_in_dollars + bill) / num_people_splitting

print(f"Each person should pay ${payment_per_person}")




