## ADD WHATEVER ARGUMENTS ARE NECESSARY TO THE MAIN FUNCTION
## IN THE SAME ORDER AS THE ARGUMENTS ARE TAKEN FROM THE
## COMMAND LINE SPECIFIED BELOW

def main(x) :
	sum1 = 0
	sum2 = 0
	i = 1
	j = 1

	while i <= x :
		if x % i == 0:
			sum1 = sum1 + 1
		i = i + 1


	while j < x and sum2 < sum1:
		sum2 = 0
		i = 1
		while i <= j:
			if j % i == 0 :
				sum2 = sum2 + 1
			i = i + 1
		j = j + 1
		
		
	if sum1 <= sum2 :
		return("not anti-prime")
	else:
		return("anti-prime")
	

## DO NOT REMOVE THIS LINE BELOW
if __name__ == "__main__" :
	import sys
	x = int(sys.argv [1])
	## MODIFY THE LINE BELOW AND ADD BEFORE WHATEVER LINES ARE NECESSARY
	## TO RUN THIS PROGRAM AS, FOR INSTANCE:
	## $ python antiprime.py 6
	## WHERE THE FIRST ARGUMENT IS A POSITIVE INTEGER NUMBER FOR WHICH
	## YOU WANT TO FIGURE OUT WHETHER IS ANTI-PRIME OR NOT
	print(main(x))
