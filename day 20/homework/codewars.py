#classwork
#1
def string_to_number(s):
  return int(s)

#1
def boolean_to_string(b):
    return str(b)

#3
def make_upper_case(s):
       return s.upper()


#4

def bool_to_word(boolean):
    if boolean == True:
            return "Yes"
    elif boolean == False:
             return "No"



#5
def make_negative( number ):
      return -abs(number)


#6
def square_sum(numbers):
        return sum(x ** 2 for x in numbers)


#7
def double_integer(i):
         return i*2



#homework

#1

def friend(x):
    names = []
    for name in x:
        if len(name) == 4:
            names.append(name)
    return names

#2

def grow(arr):
    product = 1
    for i in arr:
        product *= i 
    return product

#3

def find_average(array):
    if len(array) != 0:
        return sum(array) / len(array)
    else:
        return 0
    

#4

def goals(*x):
    return sum(x)

#5

def double_char(s):
    result = ''
    for i in s:
        result += i*2
    return result

#6

def remove_url_anchor(url):
       return url.split("#")[0]

#7

def sum_cubes(n):
      return sum(i**3 for i in range(1, n+1))

#8

def friend(x):
    names = []
    for name in x:
        if len(name) == 4:
            names.append(name)
    return names

#9

def grow(arr):
    product = 1
    for i in arr:
        product *= i 
    return product

#10

def find_average(array):
    if len(array) != 0:
        return sum(array) / len(array)
    else:
        return 0 
    
#11

def goals(*x):
    return sum(x)

#12

def double_char(s):
    result = ''
    for i in s:
        result += i*2
    return result

