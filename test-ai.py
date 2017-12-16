print 'this is the start of this simple AI. Please wait a minute...'
print '...'
print '...'
print '...'
print 'Hello, welcome back. '
print
print
print 'How are you doing today? '
feeling = raw_input()
positive_feeling = {'happy','positive','glad','energetic'}
negative_feeling = {'sad','grim','lonely'}
if feeling in positive_feeling:
	print 'I am glad that you are feeling positive today.'
if feeling in negative_feeling:
	print 'I hope you feel better soon.'

