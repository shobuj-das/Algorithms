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

import datetime

class Employee:
    def __init__(self,employee_id:int, name:str, department:str):
        self.employee_id = employee_id
        self.name = name
        self.department = department

        self.is_checked_in = False
        self.check_in_time = None
        self.check_out_time = None

    def __str__(self):
        return(
            f"ID: {self.employee_id} | "
            f"Name: {self.name} | "
            f"Department: {self.department}"
        )
    

class AttendanceSystem:
    def __init__(self):
        self.employee_list = []

    def get_employee(self, employee_id):
        for emp in self.employee_list:
            if emp.employee_id == employee_id:
                return emp
        return None
    
    def add_employee(self, employee):
        if not self.get_employee(employee_id=employee.employee_id):
            self.employee_list.append(employee)
        else:
            print("Employee already exist")

    def check_in(self,employee_id):
        for emp in self.employee_list:
            if emp.employee_id == employee_id:
                if not emp.is_checked_in:
                    emp.is_checked_in = True
                    emp.check_in_time = datetime.datetime.now()
                    return
        print("Employee id not registered")
        return None
            

    def check_out(self,employee_id):
        for emp in self.employee_list:
            if emp.employee_id == employee_id:
                if emp.is_checked_in:
                    emp.is_checked_in = False
                    emp.check_out_time = datetime.datetime.now()
                else:
                    print("Employee already checked out")
                return
        print("Employee id not registered")
        return None

    def display_all_employees(self):
        if not self.employee_list:
            print("No employees found")
            return
        for emp in self.employee_list:
            print(emp)

    def attendance_report(self):
         
        if not self.employee_list:
            print("No employee found.")
            return

        print("\n================ Attendance Report ================")

        for employee in self.employee_list:

            status = (
                "Inside Office"
                if employee.is_checked_in
                else "Outside Office"
            )

            check_in = (
                employee.check_in_time.strftime("%H:%M:%S")
                if employee.check_in_time
                else "-"
            )

            check_out = (
                employee.check_out_time.strftime("%H:%M:%S")
                if employee.check_out_time
                else "-"
            )

            print(
                f"ID: {employee.employee_id}"
                f" | Name: {employee.name}"
                f" | Dept: {employee.department}"
                f" | Status: {status}"
                f" | Check-In: {check_in}"
                f" | Check-Out: {check_out}"
            )


if __name__ == "__main__":

    attendance = AttendanceSystem()

    emp1 = Employee(101, "Shobuj", "QA")
    emp2 = Employee(102, "Rahim", "Development")
    emp3 = Employee(103, "Karim", "HR")

    attendance.add_employee(emp1)
    attendance.add_employee(emp2)
    attendance.add_employee(emp3)

    attendance.add_employee(emp1)      # Duplicate ID

    attendance.display_all_employees()

    print()

    attendance.check_in(101)
    attendance.check_in(102)

    attendance.check_in(101)           # Already checked in

    attendance.check_out(101)
    attendance.check_out(101)          # Already checked out

    attendance.check_in(999)           # Employee not found

    attendance.attendance_report()