from dataclasses import dataclass


@dataclass
class Employee:
    name: str
    department: str
    salary: float


class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, name, department, salary):
        self.employees.append(
            Employee(name, department, salary)
        )

    def sort_by_salary(self):
        self.employees.sort(
            key=lambda employee: employee.salary,
            reverse=True
        )

    def total_salary(self):
        return sum(
            employee.salary
            for employee in self.employees
        )

    def average_salary(self):
        if not self.employees:
            return 0

        return self.total_salary() / len(self.employees)

    def print_report(self):
        print("Company Report")
        print("==============")

        for employee in self.employees:
            print(
                f"{employee.name} | "
                f"{employee.department} | "
                f"${employee.salary:.2f}"
            )

        print("==============")
        print(f"Employees: {len(self.employees)}")
        print(f"Total Salary: ${self.total_salary():.2f}")
        print(f"Average Salary: ${self.average_salary():.2f}")


company = Company()

company.add_employee("Alice", "Engineering", 6200.00)
company.add_employee("Brian", "Marketing", 4700.50)
company.add_employee("Clara", "Design", 5300.75)
company.add_employee("David", "Finance", 5800.25)

company.sort_by_salary()
company.print_report()