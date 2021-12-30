#import stuff here


#create simple integrate function (Ax^n = A/(n+1)x^n+1 + C)
def integrate_simple(integrand):
    #do simple integral
    integral = ""
    coeffeciant = ""
    power = ""

    #solves just x
    if(integrand == "x"):
        integral = ".5x^2"
        return integral
    #solves just x^n
    
    #solves just Ax


    #solves in the form of integral(Ax^n)
    integrandSplit = integrand.split('x') #split the values for A and ^n
    coeffeciant = integrandSplit[0]
    for item in integrandSplit[1]:
        if(item != "^"):
            power += item
    integral = str(string_to_math(coeffeciant)/(string_to_math(power)+1))+"x^" + str(string_to_math(power)+1) + " + C"
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



def string_to_math(function): #string return value
    #take the string function and do the math it cotains EX: (6/7 + 3)
    value = eval(function) #careful doing the eval as it executes in python code found in the string
    return value

#MAIN FUNCTION

myIntegrand = "6x^7"
myIntegral = integrate_simple(myIntegrand)
print(myIntegral)