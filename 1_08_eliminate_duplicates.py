# sri sreedhar
# srisreedhar@live.com
# https://sites.google.com/site/prologsite/prolog-problems/1
'''
1.08 (**) Eliminate consecutive duplicates of list elements.

If a list contains repeated elements they should be replaced with a single copy of the element.
The order of the elements should not be changed.

Example:
?- compress([a,a,a,a,b,c,c,a,a,d,e,e,e,e],X).
X = [a,b,c,a,d,e]
'''

s=['a','a','a','a','b','c','c','a','a','d','e','e','e','e']

# find the unique values
set_s= list(set(s))

# find the count of each value
'''
for i in set_s:
	print "%s is %d times repeated"%(i,s.count(i))

	
a is 6 times repeated
c is 2 times repeated
b is 1 times repeated
e is 4 times repeated
d is 1 times repeated
'''
l1,l2=[],[]
for each in a:
	if s.count(each)==1: l1.append(each)
	else: l2.append(each)

l1.extend(l2)

# missed the order though,
# could use simple set function to do it
# shouldn't loose the order	

