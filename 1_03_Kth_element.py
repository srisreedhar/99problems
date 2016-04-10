# sri sreedhar
# srisreedhar@live.com
# given a list of values and a NUMBER, duplicate each value in the list by NUMBER
# refer link/Problem statement below
# https://sites.google.com/site/prologsite/prolog-problems/1

# 1.03 (*) Find the K'th element of a list.
# The first element in the list is number 1.
# Example:
# ?- element_at(X,[a,b,c,d,e],3).
# Find the value present in Kth Index/place
# list.index , IndexError

def kth_value(listt,index):
	try:
		print "the value for the given Index is %s"%listt[index]
	except IndexError:
		print " Index Out of Range "
		print " there are %s values in the List" %len(listt)
		print " your Index value should range from 0-%s"%(len(listt)-1)



