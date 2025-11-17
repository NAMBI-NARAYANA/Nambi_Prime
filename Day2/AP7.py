def sign(number):
    if(number>0):
        return "Positive"
    elif(number<0):
        return "Negative"
    else:
        return "Neither positive or negative number is 0"
num=input("Enter the number : ")
#assuming the input is either int or Quit 
# no other possible input
while(num!="Quit"):
    num=int(num)
    print(f"The sign of the number is : {sign(num)}")
    num=input("Enter the number : ")