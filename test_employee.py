from employee import employee_details
def test_employee_details():
    excepted_output = (
        "Emplyoee Name: Alice\n"
        "Emplyoee ID: E0110\n"
        "Department: IT\n"
        "Salary: 55000"
    )
    assert employee_details("Alice", "E0110", "IT", 55000) == excepted_output