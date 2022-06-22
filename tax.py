#aus_tax_function

#Rates
rate_2 = 0.19
rate_3 = 0.325
rate_4 = 0.37
rate_5 = 0.45

#Threshold
thresh_1 = 18200
thresh_2 = 45000
thresh_3 = 120000
thresh_4 = 180000
thresh_5 = 180001

#Inclusion
inc_1 = 5092
inc_2 = 29467
inc_3 = 51667

for tax_payable in range(3):

    income = float(input("What is your yearly salary?"))
    
    if income <= thresh_1:
        
        print("You owe $0.00")
        
    elif income >= thresh_1 and income <= thresh_2:
        print(f" You owe ${(income - thresh_1) * rate_2:,.2f}")
    elif income >= thresh_2 and income <= thresh_3:
        print(f" You owe ${inc_1 + (income - thresh_2) * rate_3:,.2f}")
    elif income >= thresh_3 and income <= thresh_4:
        print(f" You owe ${inc_2 + (income - thresh_2) * rate_4:,.2f}")
    elif income >= thresh_4 and income:
        print(f" You owe ${inc_3 + (income - thresh_3) * rate_5:,.2f}")