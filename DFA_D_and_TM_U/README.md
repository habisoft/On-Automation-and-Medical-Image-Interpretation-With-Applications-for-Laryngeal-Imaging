###################################################################################################
This document explains the usage of this software for simulating a DFA that tests
strings for membership in the language substring CoRR, where all strings are of finite
length and defined from the finite alphabet Sigma = {a, b, c, ..., z, A, B, C, ..., Z}.
Recall, substring CoRR is the language of strings that contain at least one occurance
of the substring 'CoRR'.

Author: Habib Moukalled (c) 2012-2019

FILENAME - README

This software can be used for whatever the reader likes and is provided without
warranty. The author is not responsible for anything the reader does with it.
###################################################################################################


The include software is JAVA source tested with version 1.7.0_07 of the JDK. It should work with
older versions of the JDK.

Two classes are provided, one class is Turing_Machine_U.java, an example of the universal Turing machine, is the driver program for testing the DFA D described in the paper. The second file is DFA_D.java, this class defines the DFA D, recall, a finite automaton has limited memory, usuall a few registers for defining the state transitions and the input tape is a read-only memory.

To compile simply issue:

javac Turing_Machine_U.java

from a command prompt that has been pointed to the directory of the source.

To run, issue:

java Turing_Machine_U

from a command prompt that has been pointed to the directory of the source.

The included text file "test_these_strings.txt" contains the strings to be tested for membership in the language substring CoRR. Each string is on its own line. To define your own strings simply type them into the text file and hit return.
