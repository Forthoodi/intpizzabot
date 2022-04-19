 #known bugs 
#3/04/22 - final printout not printing customer details corretly

import sys
import random 
from random import randint      

# list of random names
names  = ["Louis", "Gian", "Mikara", "Joaquin", "Tomboy", "BigBen", "Calicdan", "Barlo", "Yacob", "Marcas"]

#list of Shoes Names
shoes_names = ["Jordan 1 Retro High OG,Nike Air Max 90 Terrascape, Jordan 13 Retro Brave blue, Nike Air Max 97 Triple White Wolf Grey,Nike Air Force 1 Low Travis Scott Cactus Jack, Adidas NMD R1, adidas NMD R1 Triple Black,Jordan x Off-White Retro 2 low sneaker Jordan 4 Retro University Blue sneaker,Adidas Yeezy Foam Runner shoe,Crocs x Salehe Bembury Pollex clog,Jordan x A Ma Maniére Retro 1 sneaker"]

#list of ice cream prices
shoes_prices = [352, ,142, 236 ,174, 496, 107 ,1,227, 389, 207 , 931,388 ]

#Customer details
customer_details ={}

# list to store ordered ice cream
order_list = []
# list to store order cost
order_cost = []

#validates inputs to check if they are not blank
def not_blank(question):
    valid = False 
    while not valid: 
        response = input(question)
        if response != "": 
            return response.title()
        else:
            print("This cannot be blank")

#validates inputs to check if they are an integer - component 10
def val_int(low,high,question):
    while True: 
        try:
            num = int(input(question))
            if num >= low and num <= high: 
                return num                   
            else:
                    print(f"Please enter a number between {low} and {high}")
        except ValueError: 
            print ("That is not a valid number")
            print(f"Please enter a number between {low} and {high}")




#Welcome message - component 1 
def welcome():
    '''
Purpose: To generate a random name from the list and print out 
a welcome message
Parameters: None
Returns: None 
    '''
    num = randint(0,9)
    name = (names[num])
    print("*** Welcome to John's Creamy Delights ***")
    print("*** My name is",name, "***")
    print("***What would you like to order?***")

#Menu for click & collect or delivery - component 2 
def order_type():
    del_pick = ""
    LOW = 1 
    HIGH =  2
    question = (f"Enter a number between {LOW} and {HIGH} ")
    print ("Are you going to click and collect your items, or would you like it delivered?")
    print ("For click and collect please enter 1.")
    print ("For delivery please enter 2.")
    delivery = val_int(LOW,HIGH,question)
    if delivery == 1:
        print ("Click and Collect")
        del_pick = "click and collect"
        click_collect()
    else:
        print ("Delivery")
        print ("There wll be a $9.00 delivery charge, if you order less than 5 items")
        delivery_info()
        del_pick = "delivery"
    return del_pick

#Click and collect menu - component 3
#Basic instruction 
def click_collect():
    question = ("Please enter your name")
    customer_details ['name'] = not_blank(question) 
    print(customer_details ['name'])

    question = ("Please enter your number")
    customer_details ['phone'] = not_blank(question) 
    print(customer_details ['phone'])
    print(customer_details)

#Delivery information - component 4
def delivery_info():
    question = ("Please enter your name")
    customer_details ['name'] = not_blank(question) 
    print(customer_details ['name'])
   
    question = ("Please enter your number")
    customer_details ['phone'] = not_blank(question) 
    print(customer_details ['phone'])   
    
    question = ("Please enter your address")
    customer_details ['address'] = not_blank(question) 
    print(customer_details ['address'])
    print(customer_details)

#ice cream menu- - component 5 
def menu():
    number_icecream = 12 
    for count in range (number_icecream):
        print ("{} {} ${:.2f}" .format(count +1, icecream_names[count], icecream_prices[count]))
    
#Ice cream ordering - compotent 6 
def order_icecream():
    num_icecream = 0 
    LOW = 1
    HIGH = 12
    question = (f"Enter a number between {LOW} and {HIGH} ")
    print("How many icecreams would you like to order?")
    num_icecream = val_int(LOW,HIGH,question)

    #choose ice creams from menu 
    for item in range (num_icecream):
            while num_icecream > 0: 
                print("Please chooes your ice creams by entering the number from the menu")
                question = (f"Enter a number between {LOW} and {HIGH} ")
                icecream_ordered = val_int(LOW,HIGH,question)
                icecream_ordered = icecream_ordered -1 
                order_list.append(icecream_names[icecream_ordered])
                order_cost.append(icecream_prices[icecream_ordered])
                print("{} ${:.2f}" .format(icecream_names[icecream_ordered],icecream_prices[icecream_ordered]))
                num_icecream = num_icecream -1 

# Print order out - including if order is del or C&C,names and price of each pizza - total cost including any delivery charge
#component 7
def print_order(del_pick):
    print()
    total_cost = sum(order_cost)
    print ("Customer Details")
    if del_pick == "click and collect":
        print("Your order is for click and collect")
        print(f" \nCustomer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']}")
    elif del_pick == "delivery":
        print("Your order is for delivery")
        print(f" \nCustomer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']} \nCustomer Address: {customer_details['address']}")
    print ()
    #turn into function later so that code is not repeated so much
    print ("Order Details")
    count = 0 
    for item in order_list:
        print("Ordered: {} Cost ${:.2f}" .format(item, order_cost[count]))
        count = count+1
    print()
    if del_pick == "delivery":
        if len(order_list) >= 5:
            print ("Your order will be delivered for free")
        elif len(order_list) <= 5:
            print ("There is an additional $9.00 delivery charge")
            total_cost = total_cost + 9
    print("Total Order Cost")
    print(f"${total_cost:.2f}")
    if del_pick == "click and collect":
        print ("Thank you for your order, we'll let you know when its ready")
    elif del_pick == "delivery":
        print ("Thank you for your order, it will be delivered soon")
    
# Cancel or confirm order - component 8 
def confirm_cancel():
    LOW = 1 
    HIGH =  2
    question = (f"Enter a number between {LOW} and {HIGH} ")
    print ("Please confirm your order")
    print ("To confirm order please enter 1.")
    print ("To cancel order please enter 2.")
   
    confirm = val_int(LOW,HIGH,question)
    if confirm == 1:
        print ("Order Confirmed")
        print ("Your order will be prepared soon")
        print ("Your delicious ice cream will be with you shortly")
        new_exit()
                    

    elif confirm == 2:
        print ("Your Order has been Cancelled")
        print("You can reorder or exit")
        new_exit()          
      
        

#Option for new order or exit - component 9 
def new_exit():
    LOW = 1 
    HIGH =  2
    question = (f"Enter a number between {LOW} and {HIGH} ")
    print ("Would you like to reorder or exit")
    print ("To start another order please enter 1.")
    print ("To exit please enter 2.")
    confirm = val_int(LOW,HIGH,question)
    if confirm == 1:
        print ("New Order")
        order_list.clear
        order_cost.clear
        customer_details.clear
        main()
                    
    elif confirm == 2:
        print ("Exit")  
        order_list.clear
        order_cost.clear
        customer_details.clear
        sys.exit()
    

#Main Function 
def main():
         '''
        Purpose: To run all functions 
        a welcome message
        Parameters: None
        Returns: None 
         '''
         welcome()
         del_pick = order_type()
         menu()
         order_icecream()
         print_order(del_pick)  
         confirm_cancel()


main()