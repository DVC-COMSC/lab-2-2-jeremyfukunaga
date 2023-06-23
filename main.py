def main():
    workhours = int(input('Enter your work hours: '))
    reg_hours = 40
    reg_rate = 18.25
    ov_rate = 27.78

   ##################################################
   # Code your program here
   ##################################################
    # overtime = workhours - reg_hours
    # overtime_wage = overtime * ov_rate
    # regular_wage = reg_hours * reg_rate
    # total_wage = regular_wage + overtime_wage

    print(f"Regular hours: {reg_hours} Regular Charge: {regular_wage}")
    print(f"Overtime hours: {overtime} Overtime Charge: {overtime_wage:.2f}")
    print(f"Total wage : {total_wage:.2f}")

   ##################################################
   # Do not delete the return statement
   ##################################################
    return regular_wage, overtime_wage, total_wage


if __name__ == '__main__':
    main()

# Regular hours for the work week
reg_hours = 40

# Regular wage rate per hour
reg_rate = 18.25

# Overtime wage rate per hour
ov_rate = 27.78

# Input the employee's work hours
workhours = float(input("Enter the employee's work hours: "))

# Calculate the overtime hours
overtime_hours = max(workhours - reg_hours, 0)

# Calculate the regular wages
regular_wages = reg_hours * reg_rate

# Calculate the overtime wages
overtime_wages = overtime_hours * ov_rate

# Calculate the total wages for the week
total_wages = regular_wages + overtime_wages

# Display the total wages for the week
print("Total Wages for the Week: $", total_wages)