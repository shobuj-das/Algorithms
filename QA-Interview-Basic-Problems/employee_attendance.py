# ============================================================
# Day 18 - Employee Attendance Tracker
#
# Difficulty:
# Medium
#
# Concepts:
# - OOP
# - Dictionary
# - Exception Handling
# - Date Validation
# - Class Composition
#
# ------------------------------------------------------------
#
# Problem Statement
#
# Design an EmployeeAttendanceSystem.
#
# Create two classes:
#
# 1. Employee
# 2. AttendanceSystem
#
# Each Employee has:
#
# - employee_id
# - name
# - department
#
# The AttendanceSystem should support:
#
# add_employee(employee)
#
# check_in(employee_id)
#
# check_out(employee_id)
#
# get_employee(employee_id)
#
# display_all_employees()
#
# attendance_report()
#
# ------------------------------------------------------------
#
# Rules
#
# 1. Employee ID must be unique.
#
# 2. Cannot check in twice without checking out.
#
# 3. Cannot check out before checking in.
#
# 4. Unknown employee IDs should be handled gracefully.
#
# ------------------------------------------------------------
#
# Bonus 1
#
# Record the current check-in and check-out time.
#
# (Hint: datetime.now())
#
# ------------------------------------------------------------
#
# Bonus 2
#
# Count employees currently inside the office.
#
# ------------------------------------------------------------
#
# Bonus 3
#
# Display attendance grouped by department.
#
# ============================================================


class Employee:

    # def __init__(self, employee_id,name,department):
    #     self.employee_id = employee_id
    #     self.name = name
    #     self.department = department

    employee_list = []
    def add_employee(self, employee):
        self.employee_list.append(
            "employee_id" : self.employee_id,
            "name" : self.name
        )

class AttendanceSystem(Employee):
    
    pass


if __name__ == "__main__":
    attendance_system = AttendanceSystem
    attendance_system.add_employee(
        
    )


    