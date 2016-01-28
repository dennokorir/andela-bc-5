#test file for test cases in andelabs
#word count
'''
def words(words_input):
  word_counts = {}
  words_input = words_input.replace('\n'," ")
  words_input = words_input.replace('\t'," ")
  words_input = words_input.replace("  "," ").split(" ")


  for word in words_input:
    if word not in word_counts:
    	try:
    		word = int(word)
    		word_counts[word] = 1
    	except:

      		word_counts[word] = 1
    else:
    	try:
    		word = int(word)
    		word_counts[word] = word_counts[word] + 1
    	except:

      		word_counts[word] = word_counts[word] + 1

  return word_counts
print words('hello\nworld')
'''
#string lengths
'''
def string_length(words_input):
	string_list = []
	word_lengths = []
	if type(words_input) is not list:
		words_input = words_input.split(" ")
	for item in words_input:
		word_lengths.append(len(item))
	return word_lengths

print string_length(['Adam', 'Frankel'])
'''
#fizzbuzz
'''
def fizz_buzz(number):
	if number % 3 == 0 and number % 5 == 0:
		return "FizzBuzz"
	elif number % 5 == 0:
		return "Buzz"
	elif number % 3 == 0:
		return "Fizz"
	return number
print fizz_buzz(33)
'''
#factorial
'''
def factorial(number):
	result = 1
	if number == 0:
		return 1
	else:
		while number > 0:
			result *= number
			number -= 1
	return result
print factorial(0)
'''
#find_max_min
'''
def find_max_min(numbers):
	if min(numbers) == max(numbers):
		return [len(numbers)]
	return [min(numbers),max(numbers)]
print find_max_min([4,4,4,4,4])
'''
#find missing
'''
def find_missing(list1,list2):
	list1 = set(list1)
	list2 = set(list2)
	result = list1 ^ list2
	if len(result) == 0:
		return 0
	return result[0]
print find_missing([5, 4, 7, 6, 11, 66], [5, 4, 1, 7, 6, 11, 66])
'''
#prime checker
'''
class PrimeChecker(object):


    def __init__(self, number = 0):
        """Initialise the PrimeChecker class."""
        self.number = number


    def is_prime(self):
        try:
            for div in range(2,int(self.number)):
                if self.number % div == 0:
                   return False
            return True

        except:
            return False

test = PrimeChecker(41)
print(test.is_prime())
'''
#prime checker 2
'''
class PrimeChecker(object):
  """PrimeChecker class.

  Attributes:
    number: an integer to be tested."""

  def __init__(self, number = 0):
    """Initialise the PrimeChecker class."""
    self.number = number

  def is_prime(self):
    """Checks if the number argument is a prime number or not."""
    try:
      for i in range(2, int(self.number)):
        if int(self.number) % i == 0:
          return False
      return True
    except ValueError:
      return False
'''
#datatype
'''
def data_type(arg=None):
    if isinstance(arg,str):
        return len(arg)
    elif arg is None:
        return "no value"
    elif isinstance(arg,bool):
        return arg
    elif isinstance(arg,list):
        try:
            return arg[2]
        except:
            return None
    elif isinstance(arg,int):
        if arg > 100:
            return "more than 100"
        if arg < 100:
            return "less than 100"
        if arg > 100:
            return "Equal to 100"
'''
#reverse string
'''
def reverse_string(string=None):
    if string == None or string == "":
        return None
    new_string = string[::-1]
    if new_string == string:
        return True
    elif new_string != string:
        return new_string
print reverse_string('books')

'''
def arith_geo(args):
    if len(args) == 0:
        return 0
    diffs = [args[x]-args[x+1] for x in range(len(args)-1)]
    if max(diffs) == min(diffs):
        return "Arithmetic"
    diffs = [(args[x+1]/args[x]) for x in range(len(args)-1)]
    if max(diffs) == min(diffs):
        return "Geometric"

    return -1
print arith_geo([-128, 64, -32, 16, -8])







