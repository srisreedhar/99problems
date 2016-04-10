# sri sreedhar
# srisreedhar@live.com
# given a list of values and a NUMBER, duplicate each value in the list by NUMBER
# Input : ( [a,b,c], 2)
# Output : [a,a,b,b,c,c]
# refer link/Problem statement below
# https://sites.google.com/site/prologsite/prolog-problems/1
# 1.14 (*) Duplicate the elements of a list.
# Example:
# ?- dupli([a,b,c,c,d],X).
# X = [a,a,b,b,c,c,c,c,d,d]

# Function which takes a List and an Integer as INPUT
# No validations applied to check Zero-Division error / Float / Empty List

# duplicate(l,4)
# ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c']

def duplicate(listt,number):
	"""args : List, Integer , each value in list is replicated by Integer times"""
	temp=[]
	for i in listt:
		temp.append(i*number)
	output=[]
	for j in temp:
		output.extend(list(j))
	return output