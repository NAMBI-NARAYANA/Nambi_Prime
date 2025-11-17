def digit_print(num):
    while(num>0):
        print(num%10)
        num=int(num/10)
number=int(input("Enter the number : "))
digit_print(number)