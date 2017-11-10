user = raw_input('Hello, What is your name? -> ')
print 'Welcome, ' + user
weight = float(raw_input('Can you please tell me your weight in kilograms? -> '))
height = float(raw_input('And your height in meters? -> '))

def bmi_calculator(w, h):
 bmi = w / (h ** 2)
 print 'Hello, Your BMI is -> ' + str(bmi)
 print 'Thank you for using this program '
bmi_calculator(weight, height)
