"""
When some number of tourists get equal number of candies from 2 equal bugs
of candies one candy remians.
When same number of tourists get equal number of candies from 3 equal bugs of 
candies then 13 candies remains.
What is the number of tourists? 
"""

MAX_TOURISTS = 1000000

def find_number_of_tourists():
    tourists = 1

    while (tourists < MAX_TOURISTS):
        # if (tourists % 100 == 1):
        #     print(tourists)
        if check_number_of_tourists(tourists):
             print("SOLUTION: {}".format(tourists))
        tourists = tourists + 2

def check_number_of_tourists(tourists):
    cookies = (tourists + 1)/2
    modulos = []

    while (True):
        #print("check T={}, C={}".format(tourists, cookies))
        bugs3mod = 3*cookies % tourists

        if (bugs3mod == 13):
            print("FOUND - {}:{}".format(tourists, cookies))
            return True

        if bugs3mod in modulos:
            #print("{} is not possible".format(tourists))
            return False

        modulos.append(bugs3mod)

        cookies = cookies + tourists

find_number_of_tourists()
