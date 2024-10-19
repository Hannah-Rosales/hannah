import Activity4_Class

obj1 = Activity4_Class.Student_Info()
name = input("Enter Student Name: ")
course = input("Enter Course: ")
student_number = input("Enter Student Number: ")
academic_year = input("Enter Academic Year: ")
current_date = input("Enter Current Date: ")
student_data = obj1.get_student_data(name, course, student_number, academic_year, current_date)


while True:
    subject = input("Enter subject name (or 'done' to finish): ")
    if subject.lower() == 'done':
        break
    units = int(input(f"Enter units for {subject}: "))



    # additional fees
additional_fees = []
while True:
    fee = input("Enter additional fee (or 'done' to finish): ")
    if fee.lower() == 'done':
        break
    additional_fees.append(float(fee))





















