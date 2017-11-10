user = raw_input('Hello, What is your name? -> ')
print 'Welcome, ' + user
weight = float(raw_input('Can you please tell me your weight in kilograms? -> '))
height = float(raw_input('And your height in meters? -> '))

def bmi_calculator(w, h):
 bmi = w / (h ** 2)
 print 'Hello, Your BMI is -> ' + str(bmi)
 if bmi < 18.5:
  print 'Based on our charts, you are considered underweight, please contact your doctor for a weight gain plan'
 if bmi >= 18.5 and bmi < 25:
  print 'Based on our charts, you are considered healthy, keep up the good work'
 if bmi >= 25 and bmi < 30:
  print 'Based on our charts, you are considered overweight, please contact your doctor for a weight loss plan'
 if bmi >= 30:
  print 'Based on our charts, you are considered obese, please contact your doctor for an immediate weight loss plan'
 print 'Thank you for using this program '
bmi_calculator(weight, height)
