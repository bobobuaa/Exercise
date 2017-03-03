def is_palindrome(test):
	n=len(test)
	for i in range(len(test)//2 ):
		if test[i]!=test[n-i-1]:
			return False
	return True