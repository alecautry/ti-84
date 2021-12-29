#import stuff here


#create simple integrate function (Ax^n = A*n/(n+1)x^n+1 + C)
def integrate_simple(integrand):
    #do simple integral
    integral = ""
    integrandSplit = integrand.split('x')
    integral = integrandSplit[0]
    return integral

def integrate_trig(integrand):
    #do trig integral
    #call integrate_simple as needed
    integral = ""
    return integral

def integrate_letu(integrand):
    #let u integral
    #call other funtions as needed
    integral = ""
    return integral



def string_to_math(function):
    #take the string function and do the math it cotains EX: (6/7 + 3)
    value = eval(function) #careful doing the eval as it executes in python code found in the string
    return value

#MAIN FUNCTION

myIntegrand = "6x^7"
AbigailsNum = 34
myIntegral = integrate_simple(myIntegrand)
print(myIntegral)