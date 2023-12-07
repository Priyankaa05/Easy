# Easy
Q 1.Given a string s consisting of words and spaces, return the length of the last word in the string. A word is a maximal  substring consisting of non-space characters only.  

Explaination:

Logic:
Input:

The function takes a string s as input.
Splitting the String:

The string is split into a list of words using the split() method. This assumes that words are separated by spaces.
Checking for Words:

If there are no words in the list (i.e., the input string was empty or contained only spaces), the function returns 0.
Length of Last Word:

If there are words in the list, the function returns the length of the last word in the list.
Algorithm:
Splitting the String Algorithm:

The split() method is used to split the string into a list of words. This algorithm has a time complexity of O(n), where n is the length of the input string.
Checking for Words Algorithm:

The algorithm checks if the list of words is empty (if not words:). This operation has a time complexity of O(1) because it involves checking the length of the list.
Length of Last Word Algorithm:

If there are words, the algorithm returns the length of the last word by accessing the last element of the list (len(words[-1])). This operation also has a time complexity of O(1).

Overall Algorithm Complexity:
The overall time complexity of the algorithm is dominated by the split() operation, making it O(n), where n is the length of the input string.

The space complexity is O(m), where m is the number of words in the string since the function creates a list of words.

In summary, the algorithm efficiently splits the string into words and returns the length of the last word, handling cases where the input string is empty or contains only spaces.
