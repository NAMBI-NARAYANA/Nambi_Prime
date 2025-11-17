import random
num=random.randint(1,100)
# print(num)
guess=int(input("Enter your guess : "))
guess_count=1
while(guess!=num):
    if(guess>num):
        print("Guess is higher than the number")
    else:
        print("Guess is lower than the number")
    guess=int(input("Enter your guess : "))
    guess_count+=1
print(f"The correct number ({num}) is guessed in {guess_count}")