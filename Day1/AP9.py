P=float(input("Enter principle amount : "))
T=float(input("Enter time is years : "))
R=float(input("Enter the rate of intrest per annum : "))
Intrest=(P*T*R)/100
print(f"The amount to be paid is {P+Intrest}")