def sum_digits(num):
    sum=0
    while(num>0):
        sum+=num%10
        num=int(num/10)
    return sum
number=int(input("Enter the number : "))
print(f"The sum of digits of {number} is : {sum_digits(number)}")