
import random
from random import randint

#list of names
names = [ "Mikara", "Louis" , "Jodek " , "Karlo " ,"Tomas", "James" , "Marcus" , "Jan" , "Tomas" ]
def welcome():
    
    num = randint(0,9)
    name = (names[num])
    print ("*** Welcome to Shoes Shop  ***") 
    print("***My name is",name,"***")
    print("Here to help please order ")


def main():
         """""
    Purpose : To run all functions  
    a Welcome message
    Parameters : None 
    Returns : None 
     """
welcome()
    
 



main()