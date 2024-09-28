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





# Determine SSS contribution based on 2024 table
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
else:
    sss_contribution = 0

print("\n--- Employee Details ---")
print(f"Company Name: {company_name}")
print(f"Department: {department}")
print(f"Employee Code: {employee_code}")
print(f"Employee Name: {employee_name}")
print(f"Salary Cutoff: ${salary_cutoff:.2f}")
print(f"Rate per Hour: ${rate_per_hour:.2f}")
print(f"Working Hours: {working_hours} hours")
print(f"Overtime Hours: {overtime_hours} hours")
print(f"Absent Hours: {absent_hours} hours")
print(f"Tardy Hours: {tardy_hours} hours")
print(f"Hours Worked per Day: {hours_worked_per_day} hours")
print(f"SSS Contribution: ${sss_contribution:.2f}")
print(f"Basic Pay: ${basic_pay:.2f}")
print(f"Overtime Pay: ${overtime_pay:.2f}")
print(f"Absence Pay: ${absences_pay:.2f}")
print(f"Tardy Pay: ${tardiness_pay:.2f}")
print(f"Honorarium Pay: ${honorarium_pay:.2f}")
print(f"Gross Earning: ${gross_earn}")
