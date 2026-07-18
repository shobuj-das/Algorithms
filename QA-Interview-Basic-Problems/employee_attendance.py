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
    def __int__(self,employee_id:int, name:str, department:str):
        self.employee_id = employee_id
        self.name = name
        self.department = department

        self.is_checked_id = False
        self.check_in_time = None
        self.check_out_time = None

    def __str__(self):
        return(
            f"ID: {self.employee_id} | "
            f"Name: {self.name} | "
            f"Department: {self.department}"
        )
    

class AttendanceSystem(Employee):
    def __init__(self):
        self.employee_list = []

    def get_employee(self, employee_id):
        for emp in self.employee_list:
            if employee_id == emp.employee_id:
                return emp
        return None
    
    def add_employee(self, employee):
        if self.get_employee(employee_id=employee.employee_id):
            self.employee_list.append(employee)

    def check_id(employee_id):
        pass

    def check_out(employee_id):
        pass

    def display_all_employees():
        pass

    def attendance_report():
        pass 

if __name__ == "__main__":
   attendance = AttendanceSystem

   emp1 = Employee(101, "Shobuj", "QA")
    