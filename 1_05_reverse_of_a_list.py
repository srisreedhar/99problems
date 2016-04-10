# sri sreedhar
# srisreedhar@live.com
# given a list of values and a NUMBER, duplicate each value in the list by NUMBER
# refer link/Problem statement below
# https://sites.google.com/site/prologsite/prolog-problems/1

# 1.05 (*) Reverse a list. 

def reverse(listt):
	output=[]
	for i in range(len(listt)):
		output.append((listt[-i-1]))
	return output


# >>>l=['a','b','c']	
# >>> temp
# ['c', 'b', 'a']

# >>> for i in range(5):
# 	print i

	
# 0
# 1
# 2
# 3
# 4
# >>> for i in range(5):
# 	print (i-1)

	
# -1
# 0
# 1
# 2
# 3
# >>> for i in range(5):
# 	print (-i-1)

	
# -1
# -2
# -3
# -4
# -5


