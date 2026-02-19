#Tax Rate
#Samuel Renneke, 2/19/2026

#Calculation
def tax_calculation(sales):
    county_tax = sales * 0.025
    state_tax = sales * 0.05
    total = county_tax + state_tax
    return total, county_tax, state_tax

# Call and unpack function
total, county, state = tax_calculation(float(input("Enter the sales: ")))

# Print product
print("The county tax is ", county)
print("The state tax is ", state)
print("The total tax is ", total)
