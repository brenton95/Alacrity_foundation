

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

#Interface to check prime-ness of a single number or of numbers within a given range
if __name__ == '__main__':
  
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
