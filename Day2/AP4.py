def count_digits(num):
    count=0
    while(num>0):
        count+=1
        num=int(num/10)
    return count
number=int(input("Enter the number : "))
print(f"The number of digits in {number} is {count_digits(number)}")