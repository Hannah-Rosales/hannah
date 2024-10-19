import Activity4_Class


def main():

    name = input("Enter student name: ")
    course = input("Enter course: ")
    student_number = input("Enter student number: ")
    academic_year = input("Enter academic year: ")
    current_date = input("Enter current date (YYYY-MM-DD): ")

    student = Student(name, course, student_number, academic_year)
    academic_details = AcademicDetails()

    #subjects and units
    while True:
        subject = input("Enter subject name (or 'done' to finish): ")
        if subject.lower() == 'done':
            break
        units = int(input(f"Enter units for {subject}: "))
        academic_details.add_subject(subject, units)

    #additional fees
    additional_fees = []
    while True:
        fee = input("Enter additional fee (or 'done' to finish): ")
        if fee.lower() == 'done':
            break
        additional_fees.append(float(fee))

    downpayment = float(input("Enter downpayment: "))

    # Calculating totals
    total_due = academic_details.total_due(additional_fees, downpayment)
    payment_terms = academic_details.payment_terms(total_due)

    # Display output
    print("\n--- Student Enrollment Details ---")
    print(f"Name: {student.name}")
    print(f"Course: {student.course}")
    print(f"Student Number: {student.student_number}")
    print(f"Academic Year: {student.academic_year}")
    print(f"Date Printed: {current_date}")
    print(f"Total Units: {academic_details.total_units()}")
    print(f"Tuition Fee: P {academic_details.tuition_fee():.2f}")
    print(f"Assessment Amount:P{academic_details.assessment_amount(additional_fees):.2f}")
    print(f"Total Due: P {total_due:.2f}")
    print(f"Payment per Term: P {payment_terms:.2f}")

if __name__ == "__main__":
    main()












































