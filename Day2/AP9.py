def is_prime(num):
    if num==0 or num==1:
        return "Neither prime or composite"
    for i in range(2,num):
        if num%i==0:
            return "Composite"
    return "Prime"
number=int(input("Enter the number : "))
print(f"The entered number {number} is : {is_prime(number)}")