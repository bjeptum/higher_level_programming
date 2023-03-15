#0x13. JavaScript - Objects, Scopes and Closures

##Learning Objectives

*General:

- Why JavaScript programming is amazing
- How to create an object in JavaScript
- What this means
- What undefined means
- Why the variable type and scope is important
- What is a closure
- What is a prototype
- How to inherit an object from another *

Requirements:

* Allowed editors: vi, vim, emacs
* All your files will be interpreted on Ubuntu 20.04 LTS using node (version 14.x)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/node
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should be semistandard compliant. Rules of Standard + semicolons on top. Also as reference: AirBnB style
* All your files must be executable
* The length of your files will be tested using wc
* You are not allowed to use var **

Tasks
0. Rectangle #0

0-rectangle.js: JavaScript script that defines an empty class Rectangle.
1. Rectangle #1

1-rectangle.js: JavaScript script that defines a class Rectangle. Builds on 0-rectangle.js with:
Constructor that initializes instance attributes width and height with given parameters w and h.
2. Rectangle #2

2-rectangle.js: JavaScript script that defines a class Rectangle. Builds on 1-rectangle.js with:
If provided w and h are less than or equal to 0, creates an empty object.
3. Rectangle #3

3-rectangle.js: JavaScript script that defines a class Rectangle. Builds on 3-rectangle.js with:
Instance method print() that prints the rectangle using the X character.
4. Rectangle #4

4-rectangle.js: JavaScript script that defines a class Rectangle. Builds on 4-rectangle.js with:
Instance method rotate() that swaps the width and height of the Rectangle.
Instance method double() that multiplies the width and height of the Rectangle by 2.
5. Square #0

5-square.js: JavaScript script that defines a class Square that inherits from Rectangle.
Constructor takes one argument size.
6. Square #1

6-square.js: JavaScript script that defines a class Square that inherits from Rectangle. Builds on 5-square.js with:
Instance method charPrint(c) that prints the Square using the character c.
If c is undefined, uses the character X.
7. Occurrences

7-occurrences.js: JavaScript function that returns the number of occurrences in a list.
8. Esrever

8-esrever.js: JavaScript function that reverses a list.
9. Log me

9-logme.js: JavaScript function that prints the number of arguments already printed as well as the new argument value.
Output: <number arguments already printed>: <current argument value>
10. Number conversion

10-converter.js: JavaScript function that converts a number from base 10 to another base passed as argument.
11. Factor index

100-map.js: JavaScript script that imports an array and creates a new array with each value equal to the value of initial list times the index of the new list.
Prints both the initial and new list.
12. Sorted occurences

101-sorted.js: JavaScript script that imports a dictionary of occurrences by user ID and computes a new dictionary of user ID's by occurrences.
Prints the new dictionary.
13. Concat files

102-concat.js: JavaScript script that concatenates two files passed as arguments into a file specifed as the third argument.
Usage: ./102-concat.js fileA fileB fileC.
