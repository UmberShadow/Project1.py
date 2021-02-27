#CJ Malson
#February 20, 2021
#Intro to Python Programming
#Prof. Wright

#Ask for gender information such as M, F, Enbys

girls = int(input("How many girls are in the class? "))
boys = int(input("How many boys are in the class? "))
#Some non-binary people like myself sometimes shorten non-binary to enby.
enbys = int(input("How many non-binary students are in the class? "))

#The program will calculate percentages of student gender information.

girlsPercent = boys / (girls + boys + enbys)
boysPercent = girls / (girls + boys + enbys)
enbysPercent = enbys / (girls + boys + enbys)

#Output the results from the input
print()
printResult = ("There are {0:5.2%} girls in the class.")
print(printResult.format (girlsPercent))
print()
printResult2 = ("There are {0:5.2%} boys in the class.")
print(printResult2.format (boysPercent))
print()
printResult3 = ("There are {0:5.2%} non-binary students in the class.")
print(printResult3.format (enbysPercent))
