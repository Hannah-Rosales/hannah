
company_name = input("Enter company name: ")
department = input("Enter department: ")
employee_code = input("Enter employee's code or number: ")
employee_name = input("Enter employee's name: ")
salary_cutoff = float(input("Enter salary cutoff: "))
rate_per_hour = float(input("Enter employee's rate per hour: "))
working_hours = float(input("Enter employee's number of working hours: "))
overtime_hours = float(input("Enter number of overtime hours per day: "))
absent_hours = float(input("Enter number of absent hours per day: "))
tardy_hours = float(input("Enter number of tardy hours per day: "))
honorarium_hours = float(input("Enter number of honorarium hours per day: "))

#Basic Pay
basic_pay = rate_per_hour * working_hours
#Overtime Pay
overtime_pay = rate_per_hour * overtime_hours
#Absences Pay
absences_pay = rate_per_hour * absent_hours
#Tardiness
tardiness_pay = rate_per_hour * tardy_hours
#Honorarium
honorarium_pay = rate_per_hour * honorarium_hours

#Gross Earnings
gross_earn = basic_pay + overtime_pay + honorarium_pay

# Withholding Tax
if gross_earn <= 10417:
    withholding_tax = 0.00
elif 10417 <= gross_earn <= 16666:
    withholding_tax = 0.15
elif 16667 <= gross_earn <= 33332:
    withholding_tax = 937.50
elif 33333 <= gross_earn <= 83332:
    withholding_tax = 4270.70
elif 83333 <= gross_earn <= 333332:
    withholding_tax = 16770.70
elif gross_earn >= 333333:
    withholding_tax = 91770.70

#Philhealth Contribution
if gross_earn <= 10000.00:
    philhealth_contribution = 500
elif 10000.01 <= gross_earn <= 99999.99:
    philhealth_contribution = 450.00 or 4050.00
elif gross_earn >= 100000.00:
    philhealth_contribution = 5000.00

# Pag-Ibig Contribution
pag_ibig_contribution = 100

# SSS Contribution
if gross_earn <= 4250:
    sss_contribution = 180.00
elif 4250 <= gross_earn <= 4749.99:
    sss_contribution = 202.50
elif 4750 <= gross_earn <= 5249.99:
    sss_contribution = 225.00
elif 5250 <= gross_earn <= 5749.99:
    sss_contribution = 247.50
elif 5750 <= gross_earn <= 6249.99:
    sss_contribution = 270.00
elif 6250 <= gross_earn <= 6749.99:
    sss_contribution = 292.50
elif 6750 <= gross_earn <= 7249.99:
    sss_contribution = 315.00
elif 7250 <= gross_earn <= 7749.99:
    sss_contribution = 337.50
elif 7750 <= gross_earn <= 8249.99:
    sss_contribution = 360.00
elif 8250 <= gross_earn <= 8749.99:
    sss_contribution = 382.50
elif 8750 <= gross_earn <= 9249.99:
    sss_contribution = 405.00
elif 9250 <= gross_earn <= 9749.99:
    sss_contribution = 427.50
elif 9750 <= gross_earn <= 10249.99:
    sss_contribution = 450.00
elif 10250 <= gross_earn <= 10749.99:
    sss_contribution = 472.50
elif 10750 <= gross_earn <= 11249.99:
    sss_contribution = 495.00
elif 11250 <= gross_earn <= 11749.99:
    sss_contribution = 517.50
elif 11750 <= gross_earn <= 12249.99:
    sss_contribution = 540.00
elif 12250 <= gross_earn <= 12749.00:
    sss_contribution = 562.50
elif 12750 <= gross_earn <= 13249.99:
    sss_contribution = 585.00
elif 13250 <= gross_earn <= 13749.99:
    sss_contribution = 607.50
elif 13750 <= gross_earn <= 14249.99:
    sss_contribution = 630.00
elif 14250 <= gross_earn <= 14749.99:
    sss_contribution = 652.50
elif 14750 <= gross_earn <= 15249.99:
    sss_contribution = 675.00
elif 15250 <= gross_earn <= 15749.99:
    sss_contribution = 697.50
elif 15750 <= gross_earn <= 16249.99:
    sss_contribution = 720.00
elif 16250 <= gross_earn <= 16749.99:
    sss_contribution = 742.50
elif 16750 <= gross_earn <= 17249.99:
    sss_contribution = 765.00
elif 17250 <= gross_earn <= 17749.99:
    sss_contribution = 787.50
elif 17750 <= gross_earn <= 18249.99:
    sss_contribution = 810.00
elif 18250 <= gross_earn <= 18749.99:
    sss_contribution = 832.50
elif 18750 <= gross_earn <= 19249.99:
    sss_contribution = 855.00
elif 19250 <= gross_earn <= 19749.99:
    sss_contribution = 877.50
elif 19750 <= gross_earn <= 20249.99:
    sss_contribution = 900.00
elif 20250 <= gross_earn <= 20749.99:
    sss_contribution = 900.00
elif 20750 <= gross_earn <= 21249.99:
    sss_contribution = 900.00
elif 21250 <= gross_earn <= 21749.99:
    sss_contribution = 900.00
elif 21750 <= gross_earn <= 22249.99:
    sss_contribution = 900.00
elif 22250 <= gross_earn <= 22749.99:
    sss_contribution = 900.00
elif 22750 <= gross_earn <= 23249.99:
    sss_contribution = 900.00
elif 23250 <= gross_earn <= 23749.99:
    sss_contribution = 900.00
elif 23750 <= gross_earn <= 24249.99:
    sss_contribution = 900.00
elif 24250 <= gross_earn <= 24749.99:
    sss_contribution = 900.00
elif 24750 <= gross_earn <= 25249.99:
    sss_contribution = 900.00
elif 25250 <= gross_earn <= 25749.99:
    sss_contribution = 900.00
elif 25750 <= gross_earn <= 26249.99:
    sss_contribution = 900.00
elif 26250 <= gross_earn <= 26749.99:
    sss_contribution = 900.00
elif 27750 <= gross_earn <= 28249.99:
    sss_contribution = 900.00
elif 28250 <= gross_earn <= 28749.99:
    sss_contribution = 900.00
elif 28750 <= gross_earn <= 29249.99:
    sss_contribution = 900.00
elif 29250 <= gross_earn <= 29749.00:
    sss_contribution = 900.00
elif gross_earn >= 29750:
    sss_contribution = 900.00

print("\n--- Employee Details ---")
print(f"Company Name: {company_name}")
print(f"Department: {department}")
print(f"Employee Code: {employee_code}")
print(f"Employee Name: {employee_name}")
print(f"Salary Cutoff: {salary_cutoff:.2f}")
print(f"Rate per Hour: {rate_per_hour:.2f}")
print(f"Working Hours: {working_hours} hours")
print(f"Overtime Hours: {overtime_hours} hours")
print(f"Absent Hours: {absent_hours} hours")
print(f"Tardy Hours: {tardy_hours} hours")
print(f"Basic Pay: {basic_pay:.2f}")
print(f"Overtime Pay: {overtime_pay:.2f}")
print(f"Absence Pay: {absences_pay:.2f}")
print(f"Tardy Pay: {tardiness_pay:.2f}")
print(f"Honorarium Pay: {honorarium_pay:.2f}")
print(f"Gross Earning: {gross_earn}")
print(f"SSS Contribution: {sss_contribution:.2f}")
print(f"Withholding Tax: {withholding_tax:.2f}")
print(f"PhilHealth Contribution: {philhealth_contribution:.2f}")
print(f"Pag-Ibig Contribution: {pag_ibig_contribution:.2f}")

