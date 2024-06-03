# Alacrity_foundation
Code for task perform as part of coding challenge to check coding skill level

# Challenge
## Part A
Write some code that delivers the following features in a clean, clear, and reusable way.

Determines whether a given number is prime (whose only factors are 1 and the number itself). The approach you take should not use any library functions that provide pre-built prime related maths functions.
If the number is not prime, capture the factors in some appropriate data structure, and output them.
If the number is prime - output the string ‘Prime!’.

Hint: one way of determining if a number is prime, is to first calculate the factors of a number, and then to look at the number of factors found. To determine if a number is a factor of another, use the modulus operator (%) that gives the remainder of a division operation - a remainder of 0 means that the number is a factor. 

In other words, 10 % 3 == 1 ( 3 goes into 10, thrice times (3 + 3 + 3 == 9), with a remainder of 1 (10 - 1) ). 3 is not a factor of 10.
10 % 5 == 0 (5 goes into 10 twice (5 + 5), with no remainder - 5 is a factor of 10!	


## Extension:

If you have time, extend your application to calculate all the prime numbers in a given range.
In other words, given a min of 10 and a max of 20, your code should return a structure representing 11, 13, 17, 19.


## Part B

Create a user interface - console based or GUI - that presents the data modeled above. If implementing a graphical user interface (such as a mobile app, web application or desktop GUI), you may want to consider an appropriate layout that presents the data in a sensible way. Your solution should include any relevant source files - such as layout XML files, HTML or CSS.

Your application will need to store the data in memory. However, If you choose to use a database to write the data out to permanent storage, remember to include any files necessary to initialise the database (migrations / seeders etc).

The interface should enable a user to enter a number, and specify the bounds of the range that will be considered for prime-ness. The interface should output results of the requested operation.


