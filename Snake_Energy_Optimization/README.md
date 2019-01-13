#################################################################
This document outlines the usage of the software used for simulating snakes on synthesized kymographic images. For more details, look at the paper.

Author: Habib Moukalled (c) 2012-2019

HabiSoft, LLC

FILENAME - README

This software can be used for whatever the reader likes and is provided without warranty as long as all these remarks remain intact. The author is not responsible for anything  the reader does with the software.
#################################################################


This is a few computational examples of snakes running in an ideal situation, e.g., no noise, strong well defined edges, etc. Due to the nature of these examples, the same set of parameters can be used for all configurations.


#################################################################
Running the experiments.
#################################################################

To run the dynamic programming algorithm for optimizing snake energy on simulated kymographic image sequences. This will deform one snake on the right vocal fold of the simulated kymogram. These images are synthesized magnitude of the image gradient, a typical image feature used when snaking.


**** WINDOWS ****
In Windows, if Python and additional utilities are already installed right click on test_snake.py, and select 'edit with IDLE' as your option. This will load the script in Python's editor and debugging environment. Once the script is loaded in IDLE simply press F5 to run the simulation.

The input to the simulations for minimizing snake energy will be:

synthesized_kymogram_1.png
synthesized_kymogram_2.png
synthesized_kymogram_7.png

The output of the simulations will be images titled:

test1_out.png
test2_out.png
test3_out.png

The initial snake position will be in green and the snake will be deformed until convergence this result will be a red contour.

*** Linux/UNIX ***
In Unix or Unix like OSes issue the commands:

python test_snake.py

Enjoy!


