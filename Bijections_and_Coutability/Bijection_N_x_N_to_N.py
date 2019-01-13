'''
	This Python function defines our bijection f: N x N --> N,
	An illustration of Cantor's pairing function, an invertable
	function illustrating |N x N| = |N|, both sets have the
	same cardinality, they are countably infinite.

	Author: Habib Moukalled (c) 2012-2019

	This code is provided with no warrenty or support, and
	can be used for whatever you like.
'''

# Bijection g: N x N --> N
# where we implement the bijection f: N x N --> N, from
# section II.b in the paper.
# f(a, b) = (.5 * (a + b) * (a + b + 1)) + b

def Bijection_N_x_N_to_N(a, b):
    return (.5 * ((a + b) * (a + b + 1))) + b
    
