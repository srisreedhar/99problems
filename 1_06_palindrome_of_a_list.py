# sri sreedhar
# srisreedhar@live.com
# given a list of values and a NUMBER, duplicate each value in the list by NUMBER
# refer link/Problem statement below
# https://sites.google.com/site/prologsite/prolog-problems/1

# 1.06 (*) Find out whether a list is a palindrome.
# A palindrome can be read forward or backward; e.g. [x,a,m,a,x].


def palindrome(listt):
	output=[]
	for i in range(len(listt)):
		output.append((listt[-i-1]))
	if listt == output:
		print " Given list is a Palindrome"
	else:
		print " Given list is not a Palindrome"


# >>> palindrome(l)
#  Given list is not a Palindrome
 
# >>> palindrome(list('madam'))
#  Given list is a Palindrome