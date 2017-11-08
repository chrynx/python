print 'San mo gusto tumambay today men?'
tambayan = ['mall','pub','club','bahay']
for i in range(0, len(tambayan)):
  print str(i + 1) + ' - Tatambay tayo sa ' + tambayan[i]

choice = int(raw_input('San men? '))
print('Tara tambay tayo sa ' + tambayan[choice - 1])
