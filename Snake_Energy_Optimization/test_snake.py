#!/usr/bin/python

'''
An Active Contour (Snake) Python Class

Habib Moukalled (c) 2012-2019

HabiSoft, LLC

FILE - test_snake.py

The following source is a driver program for deforming a series of snakes on synthesized
kymographic images. These images exhibit ideal cases in which their is no noise, all edges
are strong and well defined, furthermore, the same set of parameters can be used for all
geometric objects within this class of image feature.


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

from Snaxel import Snaxel
from Snake import Snake
from get_snaxels import get_snaxels;
import numpy
import scipy
from pylab import imread, imshow, gray, mean
from matplotlib.pyplot import imsave
print ' '

# Initialize snake parameters.
alpha = 1.0
beta = 0.0
gamma = -10.0
delta_y = 3
delta_x = 0

######################################################################
# RUN experiment (1)
######################################################################

print 'Running Experiment (1)'

img = numpy.zeros((320, 1000))

row_idx = 160
contour = [];

count = 0
for i in range(0, 1000):
	contour.append((row_idx, i));


snaxels, num_snaxels = get_snaxels(contour);
#num_snaxels = 1000
print 'NUM_SNAXELS = %d.' % num_snaxels
print ' '

a = imread('synthesized_kymogram_1.png')
f = numpy.rot90(a, 2)
f = numpy.rot90(a, 2)

# Plot the snake in an image.
size_vec = numpy.shape(img);

im = numpy.zeros((size_vec[0],size_vec[1], 3));
im[:,:,0] = f;
im[:,:,1] = f;
im[:,:,2] = f;


for i in range(0, num_snaxels):
	im[snaxels[i].y, snaxels[i].x, 0] = 0.0;
	im[snaxels[i].y, snaxels[i].x, 1] = 1.0;
	im[snaxels[i].y, snaxels[i].x, 2] = 0.0;


snake = Snake(snaxels, alpha, beta, delta_y, delta_x, f, gamma)
snake.MinimizeEnergy()

for i in range(0, num_snaxels):
	im[snake.snaxels[i].y, snake.snaxels[i].x, 0] = 1.0;
	im[snake.snaxels[i].y, snake.snaxels[i].x, 1] = 0.0;
	im[snake.snaxels[i].y, snake.snaxels[i].x, 2] = 0.0;

imsave('synthesized_kymogram_1_OUTPUT.png', im);
del snake

print ' '

######################################################################
# RUN experiment (2)
######################################################################

print 'Running Experiment (2)'

img = numpy.zeros((320, 1000))

row_idx = 155
contour = [];

count = 0
for i in range(0, 1000):
	contour.append((row_idx, i));


snaxels, num_snaxels = get_snaxels(contour);
#num_snaxels = 1000
print 'NUM_SNAXELS = %d.' % num_snaxels
print ' '

a = imread('synthesized_kymogram_2.png')
f = numpy.rot90(a, 2)
f = numpy.rot90(a, 2)

# Plot the snake in an image.
size_vec = numpy.shape(img);

im = numpy.zeros((size_vec[0],size_vec[1], 3));
im[:,:,0] = f;
im[:,:,1] = f;
im[:,:,2] = f;


for i in range(0, num_snaxels):
	im[snaxels[i].y, snaxels[i].x, 0] = 0.0;
	im[snaxels[i].y, snaxels[i].x, 1] = 1.0;
	im[snaxels[i].y, snaxels[i].x, 2] = 0.0;


snake = Snake(snaxels, alpha, beta, delta_y, delta_x, f, gamma)
snake.MinimizeEnergy()

for i in range(0, num_snaxels):
	im[snake.snaxels[i].y, snake.snaxels[i].x, 0] = 1.0;
	im[snake.snaxels[i].y, snake.snaxels[i].x, 1] = 0.0;
	im[snake.snaxels[i].y, snake.snaxels[i].x, 2] = 0.0;

imsave('synthesized_kymogram_2_OUTPUT.png', im);
del snake

print ' '


######################################################################
# RUN experiment (3)
######################################################################

print 'Running Experiment (3)'

img = numpy.zeros((320, 1000))

row_idx = 150
contour = [];

count = 0
for i in range(0, 1000):
	contour.append((row_idx, i));


snaxels, num_snaxels = get_snaxels(contour);
#num_snaxels = 1000
print 'NUM_SNAXELS = %d.' % num_snaxels
print ' '

a = imread('synthesized_kymogram_7.png')
f = numpy.rot90(a, 2)
f = numpy.rot90(a, 2)

# Plot the snake in an image.
size_vec = numpy.shape(img);

im = numpy.zeros((size_vec[0],size_vec[1], 3));
im[:,:,0] = f;
im[:,:,1] = f;
im[:,:,2] = f;


for i in range(0, num_snaxels):
	im[snaxels[i].y, snaxels[i].x, 0] = 0.0;
	im[snaxels[i].y, snaxels[i].x, 1] = 1.0;
	im[snaxels[i].y, snaxels[i].x, 2] = 0.0;


snake = Snake(snaxels, alpha, beta, delta_y, delta_x, f, gamma)
snake.MinimizeEnergy()

for i in range(0, num_snaxels):
	im[snake.snaxels[i].y, snake.snaxels[i].x, 0] = 1.0;
	im[snake.snaxels[i].y, snake.snaxels[i].x, 1] = 0.0;
	im[snake.snaxels[i].y, snake.snaxels[i].x, 2] = 0.0;

imsave('synthesized_kymogram_7_OUTPUT.png', im);
del snake

print ' '
