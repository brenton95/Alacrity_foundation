# -*- coding: utf-8 -*-
"""Alacrity_challenge

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/125yWFM8roSjdUIoD96Bl8dWe3j6Z2SJn

Part A
Write some code that delivers the following features in a clean, clear, and reusable way.

Determines whether a given number is prime (whose only factors are 1 and the number itself). The approach you take should not use any library functions that provide pre-built prime related maths functions.
If the number is not prime, capture the factors in some appropriate data structure, and output them.
If the number is prime - output the string ‘Prime!’.

Hint: one way of determining if a number is prime, is to first calculate the factors of a number, and then to look at the number of factors found. To determine if a number is a factor of another, use the modulus operator (%) that gives the remainder of a division operation - a remainder of 0 means that the number is a factor.

In other words, 10 % 3 == 1 ( 3 goes into 10, thrice times (3 + 3 + 3 == 9), with a remainder of 1 (10 - 1) ). 3 is not a factor of 10.
10 % 5 == 0 (5 goes into 10 twice (5 + 5), with no remainder - 5 is a factor of 10!


Extension:

If you have time, extend your application to calculate all the prime numbers in a given range.
In other words, given a min of 10 and a max of 20, your code should return a structure representing 11, 13, 17, 19.


Part B

Create a user interface - console based or GUI - that presents the data modeled above. If implementing a graphical user interface (such as a mobile app, web application or desktop GUI), you may want to consider an appropriate layout that presents the data in a sensible way. Your solution should include any relevant source files - such as layout XML files, HTML or CSS.

Your application will need to store the data in memory. However, If you choose to use a database to write the data out to permanent storage, remember to include any files necessary to initialise the database (migrations / seeders etc).

The interface should enable a user to enter a number, and specify the bounds of the range that will be considered for prime-ness. The interface should output results of the requested operation.
"""

def factor_calculator(input_number):
  """
  function to calculate the factors of a given number

  :param
  input_number (int) : Number whose factor needs to be calculated

  :Returns
  list of factors
  """
  list_of_factors = []
  for numbers in range(1,input_number +1):
    if input_number%numbers == 0:
      list_of_factors.append(numbers)
  return list_of_factors


def prime_number_calculator(input_number):
  """
  funtion to calculate if the number is prime or not a prime number

  :param
  input_number (int) : The number which needs to be checked for prime-ness

  :Returns
   'Prime !' if the number is prime else a list containing the factors of the given number
  """
  factor_list = factor_calculator(input_number)

  if len(factor_list) == 2:
    return print('Prime !')
  else:
    return print(f'The factors of number {input_number} is {factor_list}')


def prime_number_in_range(lower_limit,upper_limit):
  """
  funtion to calculate if the user given range of numbers has prime numbers

  :param
  lower_limit (int) : The lower limit of the range
  upper_limit (int) : The upper limit of the range


  :Returns
   The lower limit and the upper limit of the range and the prime numbers between them
  """


  list_of_prime_numbers = []
  for number in range(lower_limit,upper_limit):
    answer = factor_calculator(number)
    if len(answer) == 2:
      list_of_prime_numbers.append(number)

  return print(f'The prime numbers between {lower_limit} and {upper_limit} is {list_of_prime_numbers}')

"""Interface to check prime-ness of a single number or of numbers within a given range"""

choice = input('Do you want to find the prime-ness of a single number (Yes) or of a range of numbers (No): ')

if choice.lower() == 'yes' :
  user_input_value = input("Enter your Number: ")
  prime_number_calculator(int(user_input_value))
elif choice.lower() == 'no':
  lower_value = input("Enter the lower limit of the range whose prime-ness you want to calculate: ")
  upper_value = input("Enter the upper limit of the range whose prime-ness you want to calculate: ")
  prime_number_in_range(int(lower_value),int(upper_value))
else:
  print('Incorrect value given !')