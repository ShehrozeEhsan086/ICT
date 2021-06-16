working_hours = int(input("Enter the number of hours worked in a week: "))
hourly_rate = int(input("Enter the hourly pay rate: "))
if(working_hours>40):
    overtime_hours = working_hours - 40
    overtime = overtime_hours * (hourly_rate * 1.5)
    pay = (working_hours - overtime_hours ) * hourly_rate
    gross_pay = pay + overtime
    print(f"Gross Pay is Rs.{gross_pay}")
else:
    gross_pay = working_hours * hourly_rate
    print(f"Gross Pay if Rs.{gross_pay}")