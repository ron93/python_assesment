# Using Python, have the function xoxo(str) take the str parameter
# being passed and return the string true if there is an equal number of x's and o's,
# because you cannot recieve an uneven number of hugs and kisses :-)
# otherwise return the string false. Only these two letters will be entered in the string,
# no punctuation or numbers.
# For example: if str is "xooxxxxooxo" then the output should return false because there are 6 x's and 5 o's.

#!/usr/bin/python

def Xoxo(str):
    # code goes here
    
    sub1="x"
    sub2 = "o"
    str_count = str.count(sub1)
    str_count2 = str.count(sub2)
    
    return str_count == str_count2
    


    
# keep the function call
print Xoxo("can i xxoxoxo")
