#!/usr/bin/env python3


# Calculate pi using the Leibniz formula

# Set the range of the model
r = 10000000

# Initialize denominator
k = 1

# Initialize sum
s = 0

for i in range(r):
	# even index elements are positive
	if i % 2 == 0:
		s += 4/k
	else:
		# odd index elements are negative
		s -= 4/k
	# denominator is odd
	k += 2
	
print(s)
