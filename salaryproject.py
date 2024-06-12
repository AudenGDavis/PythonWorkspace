Salary = float(input("enter hourly rate of pay"))
WordWeek = float(input("enter  how many weeks you work a week"))
formater  = '>20f'
print(f"Weekly salary "  + format(Salary, formater))
print(f"Monthly salary"  + format(Salary*4, formater))
print(f"annual salary "  + format(Salary*52, formater))