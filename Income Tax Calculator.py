gross_income = float(input("Enter the gross income: ", ))
gross_income = round(gross_income, 2)
number_of_dependents = int(input("Enter the number of dependents: ", ))

taxable_income = gross_income - 10000
taxable_income -= (3000 * number_of_dependents)
income_tax = (taxable_income * 20) / 100

print(f'The income tax is ${income_tax}')
