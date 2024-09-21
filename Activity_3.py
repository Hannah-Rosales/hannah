#Initialization

company_name = input("Enter company name: ")
department = input("Enter department: ")
employee_code = input("Enter employee's code/number: ")
employee_name = input("Enter employee's name: ")
salary_date_cutoff = input("Enter salary date cut-off: ")
pay_period = salary_date_cutoff

rate_per_hr = float(input("Enter employee's rate per hour: "))
num_wk_hrs_per_day = float(input("Enter employee's number of working hours per day: "))
num_ot_hrs_per_day = float(input("Enter Number of overtime hours per day: "))
num_abs_hrs_per_day = float(input("Enter number of absent hours per day: "))
num_td_hr_per_day = float(input("Enter number of tardy hours per day: "))
num_hrs_wrd_per_day = float(input("Enter number of hours worked per day: "))

#Basic pay
basic_pay = rate_per_hr * num_wk_hrs_per_day
#Overtime Pay
overtime_pay = rate_per_hr * num_ot_hrs_per_day
#Absences
absences_pay = rate_per_hr * num_abs_hrs_per_day
#Tardiness
tardiness_pay = rate_per_hr * num_td_hr_per_day
#Honorarium
honorarium_pay = rate_per_hr * num_hrs_wrd_per_day

#gross earnings
gross_earn = basic_pay + overtime_pay + honorarium_pay

#Withholding Tax

