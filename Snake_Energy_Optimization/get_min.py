#!/usr/bin/python

'''
An Active Contour (Snake) Python Class

Habib Moukalled (c) 2012-2019

HabiSoft, LLC

FILE - get_min.py

The following is the source for a Python Active Contour (Snake) Snaxel class. A snake is a
type of computerized spline used in many fields such as image processing, computer
vision, and medical image analysis for extracting image features. As a snake's energy
is minimized, the snake-spline will deform towards salient image features like gradient
magnitude, image intensity, and even line terminations. The vertices that describe a snake
have been termed "snaxe', in this file, we implement a function for finding the minimum of a vector.


                                    ** ATTENTION **
This software is distributed without any warrenties or technical support. However, if you
should find any bugs or issues, please report them to: habib.moukalled@gmail.com. Furthermore,
this software is intened to be used for educational and medicinal purposes. With this said,
you may download, use, modify, and redistribute this software and or its components given the
following:

    (1) This license is left in tact.

    (2) This software, and or components and algorithms are not sold.

    (3) By using this software, and or components and algorithms, you agree to the above terms.
'''

import numpy;

def get_min(vector):

    num_elements = numpy.shape(vector);
    num_elements = num_elements;

    min_value = 10000000000000000000000;
    min_idx = -1;
    for i in range(0, num_elements):
        if vector[i] < min_value:
            min_value = vector[i];
            min_idx = i;


    return min_value, min_idx;
