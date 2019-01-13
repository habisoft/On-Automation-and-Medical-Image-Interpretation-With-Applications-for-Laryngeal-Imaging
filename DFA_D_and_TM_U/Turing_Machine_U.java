/********************************************************************************
 This class defines the driver program for simulating the DFA D (from the paper)
 on input string w. The DFA D will test strings for membership in the language
 substring CoRR, that is the set of all strings over the finite alphabet
 Sigma = {a, b, c, ..., z, A, B, C, ..., Z} that contain at least one occurance
 of the string 'CoRR'.

 Author: Habib Moukalled (c) 2012-2019

 FILENAME - Turing_Machine_U.java

 This software can be used for whatever the reader likes and is provided without
 warranty. The author is not responsible for anything the reader does with it.
********************************************************************************/

import java.io.File;
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;


public class Turing_Machine_U {
    public static void main(String args[]) throws IOException {
	// Open the text file containing the strings to be tested
	// for membership in the language substring CoRR.
	BufferedReader text_file = null;
	try {
	    text_file = new BufferedReader(new FileReader("test_these_strings.txt"));
	}
	catch (IOException e) {
	    System.out.println("Error opening strings.txt for reading!" + e.getMessage());
	}
	
	// Create DFA D, an instance of a DFA that tests strings
	// for membership in the language substring CoRR.
	DFA_D D = new DFA_D();
	boolean accepted = false;

	String input_line = null;
	char[] w = {};
	int n = 0;

	while ((input_line = text_file.readLine()) != null) {
	    System.out.println(" ");
	    
	    // Convert the line that has just been read in from the text
	    // file into the string w, a character array. This string is
	    // the only thing the DFA D is allowed to have on it's input tape.
	    w = input_line.toCharArray();
	    n = w.length;

	    accepted = D.run(w, n);
	    if (accepted)
		System.out.println("DFA D *ACCEPTED* input! " + 
				   input_line + " contains substring CoRR.");
	    else
		System.out.println("DFA D *REJECTED* input! " + 
				   input_line + " does not contain substring CoRR.");
	}
	System.out.println(" ");
    }
}
