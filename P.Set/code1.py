yearly_salary = float(input("Enter yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
portion_down_paymen = 0.25
current_savings = 0.0
r = 0.04
months = 0
while current_savings < total_cost*portion_down_paymen:
    current_savings += current_savings*r/12 + yearly_salary*portion_saved/12
    months += 1
print("Number of months:", months)
