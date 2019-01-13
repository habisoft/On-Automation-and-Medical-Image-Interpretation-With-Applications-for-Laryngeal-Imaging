'''
	This Python function defines our bijection g: N x N x N --> N,
	An illustration of Cantor's pairing function, an invertable
	function illustrating |N x N x N| = |N|, both sets have the
	same cardinality, they are countably infinite.

	Author: Habib Moukalled (c) 2012-2019

	This code is provided with no warrenty or support, and
	can be used for whatever you like.
'''

# Import the bijection f, the be used for function composition.
from Bijection_N_x_N_to_N import Bijection_N_x_N_to_N


# Bijection g: N x N x N --> N
# where we make use of the bijection f: N x N --> N
# to obtain g of the form:
# g(a, b, c) = (.5 * (a + f(b, c)) * (a + f(b, c) + 1)) + f(b, c)

def Bijection_N_x_N_x_N_to_N(a, b, c):
    return .5 * (a + Bijection_N_x_N_to_N(b, c)) * \
        (a + Bijection_N_x_N_to_N(b, c) + 1) + Bijection_N_x_N_to_N(b, c)

