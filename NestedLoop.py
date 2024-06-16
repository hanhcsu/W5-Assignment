# Write a program to collect data and calculate the average rainfall over a period of years:
# prompt the user for the number of years:
years = int(input("Please enter the number of years: "))
data = []
for i in range(years):
    print(f"YEAR {i + 1}")
    months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
    for j in months:
        # Prompt the user to enter the amount of rainfall for that month:
        rainfall = float(input(f"Please enter the amount of rainfall in {j} in inches: "))
        # Add the rainfall amount to the list:
        data.append(rainfall)
print(f"Number of months: {years * 12}")
print(f"Total rainfall: {sum(data):.2f} inches")
print(f"Average rainfall: {sum(data) / len(data):.2f} inches")