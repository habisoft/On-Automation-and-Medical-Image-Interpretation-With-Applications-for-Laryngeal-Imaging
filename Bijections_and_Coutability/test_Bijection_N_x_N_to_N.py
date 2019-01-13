# A script to test our biject f:N x N --> N
# A pair of natural numbers to a single natural number.


from Bijection_N_x_N_to_N import Bijection_N_x_N_to_N


# Print the first 12 Natural numbers
# using the bijection f:N_x_N --> N.

print ' '
print 'f:(0, 0) --> %d.' % Bijection_N_x_N_to_N(0, 0) # 0.
print 'f:(1, 0) --> %d.' % Bijection_N_x_N_to_N(1, 0) # 1.
print 'f:(0, 1) --> %d.' % Bijection_N_x_N_to_N(0, 1) # 2.
print 'f:(2, 0) --> %d.' % Bijection_N_x_N_to_N(2, 0) # 3.
print 'f:(1, 1) --> %d.' % Bijection_N_x_N_to_N(1, 1) # 4.
print 'f:(0, 2) --> %d.' % Bijection_N_x_N_to_N(0, 2) # 5.
print 'f:(3, 0) --> %d.' % Bijection_N_x_N_to_N(3, 0) # 6.
print 'f:(2, 1) --> %d.' % Bijection_N_x_N_to_N(2, 1) # 7.
print 'f:(1, 2) --> %d.' % Bijection_N_x_N_to_N(1, 2) # 8.
print 'f:(0, 3) --> %d.' % Bijection_N_x_N_to_N(0, 3) # 9.
print 'f:(4, 0) --> %d.' % Bijection_N_x_N_to_N(4, 0) # 10.
print 'f:(3, 1) --> %d.' % Bijection_N_x_N_to_N(3, 1) # 11.
print 'f:(2, 2) --> %d.' % Bijection_N_x_N_to_N(2, 2) # 12.
print 'f:(1, 3) --> %d.' % Bijection_N_x_N_to_N(1, 3) # 13.
print ' '
