from pprint import pprint
from random import shuffle
from random import randrange
num  = input('How many dice?')
sides= input('How many sides per die?')
sum  = 0
for i in range(num):
	sum +=randrange(sides)+1
print 'The Result is',sum
	
values = range(1,11) + 'Jack Queen King'.split()
suits  ='diamods clubs hearts spades'.split()
deck   =['%s of %s' % (v,s) for v in values for s in suits]
pprint(deck[:12])

shuffle(deck)
pprint(deck[:12])
while deck:
	raw_input(deck.pop())
	
