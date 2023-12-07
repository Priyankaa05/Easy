# Easy
Q 1.Given a string s consisting of words and spaces, return the length of the last word in the string. A word is a maximal  substring consisting of non-space characters only.  

Explaination:
def length_of_last_word(s):
This line defines a function named length_of_last_word that takes a string s as its parameter.
    s = s.rstrip()
rstrip() is a method in Python that removes trailing whitespaces (including spaces, tabs, and newlines) from the right end of a string. Here, it's used to remove trailing spaces from the input string s.

    length = 0
This line initializes a variable length to 0. This variable will be used to store the length of the last word in the string.

    for char in reversed(s):
This line starts a for loop that iterates through each character in the reversed version of the string s. reversed(s) returns a reverse iterator of the string.

        if char == ' ':
This line checks if the current character (char) is a space.

            break
If the current character is a space, the break statement is executed, which exits the for loop. This is because the goal is to find the length of the last word, and spaces indicate the end of a word.

        length += 1
If the current character is not a space, the length variable is incremented by 1. This is done to count the characters of the last word.

    return length
After the loop, the function returns the final value of the length variable, representing the length of the last word.
print(length_of_last_word("Hello World")) 
print(length_of_last_word("   fly me   to   the moon  ")) 
print(length_of_last_word("luffy is still joyboy")) 
These lines call the length_of_last_word function with different input strings and print the results. They serve as test cases for the function.
Overall, the function aims to find the length of the last word in a string by iterating through its characters from right to left, counting characters until a space is encountered, and then returning the length.
