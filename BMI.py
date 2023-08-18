#Hello, we are going to make a simple BMI calculator

#We'll add name for aesthetic purposes
def name(name):
    return(name)

user_name = (input("What is your name? "))

Username = name(user_name)

print("Hello,", Username,".......Welcome to a BMI calculator creaeted using python")

#first we need to add a define function 
#(height) and (weight) are called parameters in the function
def bodymassindex(weight,height):
    return round((weight / height**2),2)

#getting input for user using variable
#since we're putting inputs in a string format, we'll convert them into floats to allow us to perform mathematical operations using the variables
w = float(input("Enter your weight(in kilograms):  "))
h = float(input("Enter your height (in meters): "))


#we'll use a function call to bodymassindex with (h) and (w) as arguments 
#we'll assign the function call to the variable (bmi)
bmi = bodymassindex(w,h)
print('Your BMI is:', bmi)

#we'll use the conditions 
if bmi <= 18.5:
    print("You're underweight,", Username)
elif 18.6 < bmi < 24.99:
    print("You're Normal,", Username)
elif 25 < bmi < 29.29:
    print("You're overweight,", Username)
else:
    print("You're obese,", Username)

