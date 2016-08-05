#import random
# declare main () method
# allow user input
# use if statement

import random

def main():#start of main() method
    user = raw_input("Would you want a strong password or a weak password?" "\n")#allow user input

    if user == "Strong" or user == "strong" or user == "STRONG":#condition
        my_char = "wertyuiop[234567890XCVBNM<>?}|?<>"
        pw_length = 19
        password = ""

        for g in range(pw_length):
            rand_store = random.randrange(len(my_char) )
            password = password + my_char[rand_store]

        return password

    elif user == "Weak" or user == "weak" or user == "WEAK":
        weak_char = "Shiko", "Rahima", "Karanu", "Gare", "Harry", "boobs"
        return random.choice(weak_char)

    else:
        return "Sorry, wrong input. Try again."

if __name__ == "__main__":# this is where the main() method executes
    print main()






