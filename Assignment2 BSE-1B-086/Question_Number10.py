def displayEmployee(record):
    sum_total_hours_employees = []
    sum_hours_employee = 0
    week_day=0
    hours_employee = []
    employees_record = []
    x=0
    while x!=record:
        employees_record.append(x)
        print(f"Please enter the working hours of employee {x} (Sequence starts from Sunday and ends on Saturnday[1 week total].")
        for day in range(0,7):
            value = int(input("Enter the working hours: "))
            hours_employee.append(value)
            if day==6:

                while week_day < len(hours_employee):
                    sum_hours_employee = hours_employee[week_day] + hours_employee[week_day+1] + hours_employee[week_day+2] + hours_employee[week_day+3] + hours_employee[week_day+4] + hours_employee[week_day+5] + hours_employee[week_day+6]
                    sum_total_hours_employees.append(sum_hours_employee)
                    employees_record.append(sum_hours_employee)
                    sum_hours_employee = 0
                    week_day += 7
        x +=1 
    sum_total_hours_employees.sort(reverse=True)
    print("        \tSun\tMon\tTue\tWed\tThur\tFri\tSat")
    employe = 0
    for i in range(0,len(hours_employee),7):
        print(f"Employee {employe}\t{hours_employee[i]}\t{hours_employee[i+1]}\t{hours_employee[i+2]}\t{hours_employee[i+3]}\t{hours_employee[i+4]}\t{hours_employee[i+5]}\t{hours_employee[i+6]}")
        employe += 1
    print()
    for i in range(0,len(sum_total_hours_employees)):
        for j in range(0,len(employees_record)):
            if sum_total_hours_employees[i] == employees_record[j]:
                if employees_record[j-1] < len(sum_total_hours_employees):
                    print(f"Employee {employees_record[j-1]} worked for {sum_total_hours_employees[i]} hours")

def main():
    num_employees = eval(input("Enter the total number of employees: "))
    displayEmployee(num_employees)

main()

# Shehroze Ehsan 086 