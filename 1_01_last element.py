# sri sreedhar
# srisreedhar@live.com
# given a list of values and a NUMBER, duplicate each value in the list by NUMBER
# Input : ( [a,b,c], 2)
# Output : [a,a,b,b,c,c]
# refer link/Problem statement below
# https://sites.google.com/site/prologsite/prolog-problems/1
# 1.01 (*) Find the last element of a list.
# Example:
# ?- my_last(X,[a,b,c,d]).
# X = d
# function is not required, simple indexing

def last(listt):
	print "The last element is",listt[-1]

# def last(listt):print "the last element is %s "%listt[-1]	
