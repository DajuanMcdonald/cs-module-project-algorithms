'''
Input: a List of integers where every int except one shows up twice
Returns: an integer

input: array
output: integer [9]

'''


def single_number(ar):
	# loop list
	# number = ar[0]
	# for i in range(1, num):
	# 	# xor of all elements
	# 	number = number ^ar[i]
	# # return number

	# or think about python's set, it is iterable and has no duplicates
	# this datastructure is a hashtable, as it is pointless to use list manipulation
	# since the list is unordered, i.e 1 is coming before 0 and 5 and 4 are before 3.
	return 2 * sum(set(ar)) - sum(ar)


if __name__ == '__main__':
	# Use the main function to test your implementation
	arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

	print(f"The odd-number-out is {single_number(arr)}")
