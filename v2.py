from tkinter.messagebox import QUESTION


1

def order_type():
    while True:
        try:  
            num=int(input())
            if num >= 1 and num <= 2:
                return num 
            else:
                print("pick a number between 1 or 2")
        
        except ValueError:
            print("this is not a valid number")
            print ("please pick a number between 1 or 2")

LOW = 1
HIGH = 2

question = ("print a number between", LOW, "or", HIGH)

answer = order_type()

print(answer)