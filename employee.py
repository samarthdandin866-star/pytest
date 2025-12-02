
def employee_details(name, emp_id, department, salary):
    result=(
    f"Emplyoee Name: {name}\n"
    f"Emplyoee ID: {emp_id}\n"
    f"Department: {department}\n"
    f"Salary: {salary}"
    )
    return result

if __name__=="__main__":
    name= "Alice" 
    emp_id= "E0110"
    department= "IT"
    salary= 55000
    print(employee_details(name, emp_id, department, salary))
