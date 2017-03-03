import re
pattern = re.compile(r'hello')

match1=pattern.match('hello world')
match2=pattern.match('helloo world')
match3=pattern.match('helllo world')

if match1:
	print match1.group()
else:
	print 'match1 matched failed'

if match2:
	print match2.group()
else:
	print 'match2 matched failed'

if match3:
	print match3.group()
else:
	print 'match3 matched failed'

m=re.match(r'Wang', 'wang hai bo Wang',re.I)
print m.group()
print m.lastindex
print m.pos

print '\na simple Match Instance\n'
m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')  
  
print "m.string:", m.string  
print "m.re:", m.re  
print "m.pos:", m.pos  
print "m.endpos:", m.endpos  
print "m.lastindex:", m.lastindex  
print "m.lastgroup:", m.lastgroup  
  
print "m.group():", m.group()  
print "m.group(1,2):", m.group(1, 2)  
print "m.groups():", m.groups()  
print "m.groupdict():", m.groupdict()  
print "m.start(2):", m.start(2)  
print "m.end(2):", m.end(2)  
print "m.span(2):", m.span(2)  
print r"m.expand(r'\g<2> \g<1>\g<3>'):", m.expand(r'\2 \1\3') 

print '\na simple Pattern Instance\n'
p = re.compile(r'(\w+) (\w+)(?P<sign>.*)', re.DOTALL)  
   
print "p.pattern:", p.pattern  
print "p.flags:", p.flags  
print "p.groups:", p.groups  
print "p.groupindex:", p.groupindex 

