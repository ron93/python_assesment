#!/usr/bin/python
import random

def main():
    user = raw_input("Do you want a strong or a weak password " "\n")
    if  user == "Strong" or user== "strong":
    #declared var holding password characters
        text = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890!@#$%&*"
            #var to specify password length
        password_length = 16

            #var to hold password generated
        password = ""

            #loop for random password generation
        for x in range(password_length):
                #next_char holds the password generated at each index randomly chosen 
            next_char = random.randrange(len(text))
            password = password +text[next_char]

        return password
        
    elif user == "Weak" or user == "weak":
        choices = "password","incorect","jonny","aki" ,"mundu"
            #var to specify password length
            #call a method to chose a password from the listed password
        return random.choice(choices)
    
    else:
        #for invalid input
        return "wrong entry try again"
if __name__ == "__main__":
    print main()
            
    

