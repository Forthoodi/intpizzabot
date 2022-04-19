
print ("Do want to buy in store or get it delivered ")

print("For instore pick 1") 
print ("for delivery pick 2")

delivery = int(input())

low = 1
high = 2 

while True:
    try:
        delivery = int(input())

        if delivery == 1:
            print ("Delivery")
     
        if delivery == 2:
         print ("In store")


        else:
            print ("That is in not a option ")

    except ValueError:
        print("That is not a valid number ")
        print("Please enter 1 or 2 ")
