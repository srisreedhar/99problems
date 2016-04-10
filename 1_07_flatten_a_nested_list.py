# sri sreedhar
# srisreedhar@live.com
# given a list of values and a NUMBER, duplicate each value in the list by NUMBER
# refer link/Problem statement below
# https://sites.google.com/site/prologsite/prolog-problems/1
# 1.07 (**) Flatten a nested list structure
'''
Flatten a nested list structure.
Transform a list, possibly holding lists as elements into a 'flat' list by replacing each list with its elements (recursively).

Example:
?- my_flatten([a, [b, [c, d], e]], X).
X = [a, b, c, d, e]

Hint: Use the predefined predicates is_list/1 and append/3 
'''
# isinstance(object,object_type) returns boolean
# isinstance(2427,int) --> True

listt = [1,2,3,[4,[5,[6,7,8],9,10]]]

# need to identify which one of these values in the list is a 'list', this is recurrsive
# for each in listt:
# 	if isinstance(each,list):
# 		for each_2 in each:
# 			if isinstance(each_2,list):
# 				print each_2
# This would go on, on and on ..

# a quick search resulted in 
# http://stackoverflow.com/questions/2158395/flatten-an-irregular-list-of-lists-in-python
# http://stackoverflow.com/questions/909092/why-is-the-compiler-package-discontinued-in-python-3
# They included it in Py3

# This looks provoking,
# https://docs.python.org/2/library/compiler.html#module-compiler.ast
# need to spend with this post W-O
# for now,

def flatten(listt):
	from compiler.ast import flatten
	return flatten(listt)
	










