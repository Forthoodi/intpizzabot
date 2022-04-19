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
   

print ("print a number between 1 or 2 ")

answer = order_type()

print(answer)