import math
print("GLOBAL HUNGER INDEX"+ '\n' +"To Calculate the GHI we need some info as given below " + '\n' + "PUN : Proportion of the population that is undernourished " + '\n' + "CUW : Prevalance of underweight in children under five" + '\n' + "CM : proportion of children dying before the age of five"  )
#Info required to calculate the GHI of a Country 
country=str(input("Enter the name of the Country whose GHI is to be calculated"))
PUN = float(input("Enter PUN : "))
CUW = float(input("Enter CUW : "))
CM = float(input("Enter CM : "))
PUN_P = float(PUN/100)
CUW_P = float(CUW/100)
CM_P = float(CM/100)
GHI=float((PUN_P + CUW_P + CM_P)/3)
if(GHI<=9.9):
    print(country +"low GHI")
if (GHI >=10.0 and GHI<= 19.9):
    print(country +"has moderate GHI")
if(GHI >=20.0 and GHI <= 34.9):
    print(country +"has  Serious GHI")
if(GHI>= 35.0 and GHI <= 49.9):
    print(country +"has  Alarming GHI")
elif(GHI>+50.0):
    print(country+"has a Extremely Alarming GHI")

