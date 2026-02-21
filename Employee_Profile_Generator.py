from dataclasses import dataclass


@dataclass
class EmployeeProfile:
    """Represents an employee profile with associated details and code parsing."""
    first_name: str
    last_name: str
    age: int
    address: str
    position: str
    salary: int
    experience_years: float
    employee_code: str

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @property
    def experience_info(self) -> str:
        return f"Experience: {self.experience_years} years"

    def generate_employee_card(self) -> str:
        return (f"Employee: {self.full_name} | Age: {self.age} | "
                f"Address: {self.address} | Position: {self.position} | "
                f"Salary: ${self.salary:,}")

    def get_department(self) -> str:
        return self.employee_code[0:3]

    def get_year(self) -> str:
        return self.employee_code[4:8]

    def get_initials(self) -> str:
        return self.employee_code[9:11]

    def get_id_number(self) -> str:
        return self.employee_code[-3:]


def main() -> None:
    full_address = "123 Main Street, Apartment 4B"

    employee = EmployeeProfile(
        first_name="John",
        last_name="Doe",
        age=28,
        address=full_address,
        position="Data Analyst",
        salary=75000,
        experience_years=5.5,
        employee_code="DEV-2026-JD-001"
    )

    print(employee.generate_employee_card())
    print(employee.experience_info)
    
    print("\n--- Code Breakdown ---")
    print(f"Department: {employee.get_department()}")
    print(f"Year:       {employee.get_year()}")
    print(f"Initials:   {employee.get_initials()}")
    print(f"ID Number:  {employee.get_id_number()}")


if __name__ == "__main__":
    main()