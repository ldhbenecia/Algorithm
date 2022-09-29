income = int(input("Please enter your income: "))
RATE1 = 0.06
RATE2 = 0.15
RATE3 = 0.24
RATE4 = 0.35
RATE5 = 0.38

STANDARD1 = 12000000
STANDARD2 = 46000000
STANDARD3 = 88000000
STANDARD4 = 300000000

if income <= STANDARD1:
	TAX = income * RATE1
	print("Your tax is %.2f" %(TAX))
	
if STANDARD1 < income <= STANDARD2:
	TAX = (STANDARD1 * RATE1) + (income - STANDARD1) * RATE2 
	print("Your tax is %.2f" %(TAX))
	
if STANDARD2 < income <= STANDARD3:
	TAX = (STANDARD1 * RATE1 + 34000000 * RATE2) + (income - STANDARD2) * RATE3
	print("Your tax is %.2f" %(TAX))
	
if STANDARD3 < income <= STANDARD4:
	TAX = (STANDARD1 * RATE1 + 34000000 * RATE2 + 42000000 * RATE3) + (income - STANDARD3) * RATE4
	print("Your tax is %.2f" %(TAX))
	
if STANDARD4 < income:
	TAX = (STANDARD1 * RATE1 + 34000000 * RATE2 + 42000000 * RATE3 + 212000000 * RATE4) + (income - STANDARD4) * RATE5
	print("Your tax is %.2f" %(TAX))
	