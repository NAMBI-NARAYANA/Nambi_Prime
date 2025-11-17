def func(num1,num2):
    for i in range(num1,num2+1):
        if i%2==0:
            print(i)
a=int(input("Enter the start number : "))
b=int(input("Enter the ending number : "))
func(a,b)