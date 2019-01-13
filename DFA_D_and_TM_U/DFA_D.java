/********************************************************************************
 This class defines the deterministic finite automaton (DFA) D. The DFA D will 
 test strings for membership in the language substring CoRR, that is the set of 
 all strings over the finite alphabet Sigma = {a, b, c, ..., z, A, B, C, ..., Z} 
 that contain at least one occurance of the string 'CoRR'.

 Author: Habib Moukalled (c) 2012-2019

 FILENAME - DFA_D.java

 This software can be used for whatever the reader likes and is provided without
 warranty. The author is not responsible for anything the reader does with it.
********************************************************************************/

public class DFA_D{
    /*
      BEGINNING of read-only registers built into the definition of the DFA 
      for recognizing the language substring CoRR. 
    */

    // These five read-only registers define the DFA's set of states.
    private static int q_0 = 0;
    private static int q_1 = 1;
    private static int q_2 = 2;
    private static int q_3 = 3;
    private static int q_4 = 4;

    // This read-only register defines the DFA's start state.
    // Note all finite automata have only a single start state.
    private static int initial_state = q_0;

    // This read-only register defines the DFA's accepting state.
    // Note that finite automata can have more than one final/accepting state.
    private static int accepting_state = q_4;

    /* 
       END of read-only registers built into the definition of the DFA. 
    */


    /*
      BEGINNING of the read/write registers built into the definition of the DFA
      that recognizes the language substring CoRR. 
    */
    private int current_state = initial_state;
    private char input_symbol = ' ';
    private int counter = 0;
    /* 
       END of read/write register built into the definition of the DFA. 
    */

    // This function will simulate the DFA on the input string w of length n.
    // The string is formatted as a character array by some higher level
    // process. The ONLY thing on this DFA's input tape is the string w.
    public boolean run(char[] w, int n) {
	// Initialize the read/write registers for the simulation.
	current_state = initial_state;
	input_symbol = ' ';
	counter = 0;

	while (counter <= n - 1) {
	    input_symbol = w[counter];
	    current_state = delta(current_state, input_symbol);

	    if (current_state == accepting_state) {
		// The DFA successfully found the string 'CoRR' while
		// scanning its input tape. ACCEPT the string w!
		return true;
	    }
	    counter += 1; // incrument the character counter.
	}

	// The DFA reaches the end of its input tape without ever finding
	// the 'CoRR', REJECT the string w!
	return false;	    
    }
    

    // At the heart of every automoton is it's transition function. This defines
    // the behavior of the DFA.
    public int delta(int state, char symbol) {
	switch (state) {
	case 0:
	    if (symbol == 'C')
		state = q_1;
	    else
		state = q_0;
	    break;

	case 1:
	    if (symbol == 'o')
		state = q_2;
	    else
		state = q_0;
	    break;

	case 2:
	    if (symbol == 'R')
		state = q_3;
	    else
		return q_0;
	    break;

	case 3:
	    if (symbol == 'R')
		state = q_4;
	    else
		state = q_0;
	    break;
	}
	return state;
    }
}
