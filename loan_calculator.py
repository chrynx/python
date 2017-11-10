print '--------------------'
print 'Welcome to this loan calculator program'
print '--------------------'
user = raw_input('Can you please enter your name? -> ')
print
print 'Hello there, ' + user
print
amount = int(raw_input('Can you please input the amount of the loan you wish to take? -> '))
print
amount_confirm = raw_input('So you want to take a loan of ' + str(amount) + '? Is this correct? (y/n)')
while amount_confirm != 'y':
 amount = int(raw_input('Can you please input the amount of the loan you wish to take? -> '))
 amount_confirm = raw_input('So you want to take a loan of ' + str(amount) + '? Is this correct? (y/n)')
print
print 'Thank you'
print '--------------------'
months = int(raw_input('Now can you please state over how many months do you want to repay this loan? -> '))
print
months_confirm = raw_input('So you want to repay the loan over ' + str(months) + ' months? (y/n)')
while months_confirm != 'y':
 months = int(raw_input('Now can you please state over how many months do you want to repay this loan? -> '))
 months_confirm = raw_input('So you want to repay the loan over ' + str(months) + ' months? (y/n)')
print
print 'Thank you'
print '--------------------'
interest = float(raw_input('Now please state the interest rate of which the loan is to be agreed upon -> '))
print
interest_confirm = raw_input('So the interest rate of the loan is ' + str(interest) + '%, Is this correct? (y/n)')
while interest_confirm != 'y':
 interest = float(raw_input('Now please state the interest rate of which the loan is to be agreed upon -> '))
 interest_confirm = raw_input('So the interest rate of the loan is ' + str(interest) + '%, Is this correct? (y/n)')
print 
print 'Thank you'
print '--------------------'
print 'We are now calculating your monthly payable amount'
for i in range(3):
 print 'Calculating...'
def loan_calculator(a,m,i):
 monthly = (a + (a * (i / 100) ) ) / m
 print 'Your total monthly payable is ' + str(monthly)
 print '--------------------'
 print 'Thank you for using this program'
 print 'Goodbye'
 exit()
loan_calculator(amount, months, interest)
