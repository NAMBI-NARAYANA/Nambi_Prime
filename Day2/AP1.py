salary=int(input("Enter your salary : "))
if salary<30000:
    if(salary<0):
        print("Salaty can't be negative")
    else:
        tax=(salary*5)/100
elif (salary>=30000 and salary<70000):
    tax=(salary*15)/100
else:
    tax=(salary*25)/100
print(f"Tax to be paid Rs.{tax}")