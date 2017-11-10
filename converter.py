print '--------------------------------------------------'
print 'Python Converter Program'
print '--------------------------------------------------'
print 'Thank you for choosing this program'

def exit_prompt():
 again = raw_input('Is that all for today? (y/n)')
 while again != 'y' and again != 'n':
  again = raw_input('Is that all for today? (y/n)')
 if again == 'y':
  print 'Thank you for using this program'
  print 'Goodbye'
  exit()
 if again == 'n':
  convert()

def convert():
 print 'What would you like to convert today? '
 units = ['KGS - LBS', 'FT - INCHES', 'KMS - MILES']
 for i in range(0,len(units)):
  print str(i + 1) + ') ' + units[i]
 convert_choice = int(raw_input('Please enter the number of the conversion you wish to make -> ' ))
 convert_choice = convert_choice - 1
 print 'So you want to convert ' + units[convert_choice] + ' today, very well'

 if convert_choice == 0:
  print 'Which way are we going today? '
  print '1) KGS => LBS'
  print '2) LBS => KGS'
  base = int(raw_input('Please choose the number of your choice -> '))
  if base == 1:
   KG = int(raw_input('Amount in KGS -> '))
   print 'This is the amount in LBS -> ' + str(KG * 2.2)
  if base == 2:
   LBS = int(raw_input('Amount in LBS -> '))
   print 'This is the amount in KGS -> ' + str(LBS / 2.2)

 if convert_choice == 1:
  print 'Which way are we going today? '
  print '1) FT => INCHES'
  print '2) INCHES => FT'
  base = int(raw_input('Please choose the number of your choice -> '))
  if base == 1:
   FT = int(raw_input('Amount in FT -> '))
   print 'This is the amount in INCHES -> ' + str(FT * 12)
  if base == 2:
   INCHES = int(raw_input('Amount in INCHES -> '))
  print 'This is the amount in FT -> ' + str(INCHES / 12)
 
 if convert_choice == 2:
  print 'Which way are we going today? '
  print '1) KMS => MILES'
  print '2) MILES => KMS'
  base = int(raw_input('Please choose the number of your choice -> '))
  if base == 1:
   KMS = int(raw_input('Amount in KMS -> '))
   print 'This is the amount in MILES -> ' + str(KMS * 1.6)
  if base == 2:
   MILES = int(raw_input('Amount in MILES -> '))
   print 'This is the amount in KMS -> ' + str(MILES / 1.6)
 exit_prompt()
convert()
