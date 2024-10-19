class Student:
    def __init__(self, name, course, student_number, academic_year):
        self.name = name
        self.course = course
        self.student_number = student_number
        self.academic_year = academic_year

class AcademicDetails:
    def __init__(self):
        self.subjects = []
        self.units = []

    def add_subject(self, subject, units):
        self.subjects.append(subject)
        self.units.append(units)

    def total_units(self):
        return sum(self.units)

    def tuition_fee(self):
        return self.total_units() * 1551.00

    def assessment_amount(self, additional_fees):
        return self.tuition_fee() + sum(additional_fees)

    def total_due(self, additional_fees, downpayment):
        return self.assessment_amount(additional_fees) - downpayment

    def payment_terms(self, total_due):
        return total_due / 3
