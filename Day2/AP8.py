def calc(num1,num2,operation):
    match operation:
        case "+":
            return num1+num2
        case "-":
            return num1-num2
        case "*":
            return num1*num2
        case "/":
            return num1/num2
        case _:
            print("The operator is not valid")
number1=int(input("Enter num1 : "))
number2=int(input("Enter num2 : "))
operator=input("Enter the operator : ")
print(f"{number1}{operator}{number2}={calc(number1,number2,operator)}")