# Using Python, have the function xoxo(str) take the str parameter
# being passed and return the string true if there is an equal number of x's and o's,
# because you cannot recieve an uneven number of hugs and kisses :-)
# otherwise return the string false. Only these two letters will be entered in the string,
# no punctuation or numbers.
# For example: if str is "xooxxxxooxo" then the output should return false because there are 6 x's and 5 o's.


#declare method
#declare two variables to hold the letters to be counted
#declare two other variables to hold count result
#compare the two count variables
#return result


def xoxo(str): #declare method
    sub = "x"#assign value to inital variable
    sub2 = "o"#assign value to inital variable

    str_count = str.count(sub)#assign count result to another variable
    str_count2 = str.count(sub2)#assign count result to another variable

    return str_count == str_count2#comapare equality of count results

print xoxo("xoxxxxooooxowe")#call method