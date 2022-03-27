from collections import Counter
import datetime
from functools import reduce
from itertools import count
from operator import countOf
import time

def my_decorator(func): #task 5.1
    """Prints date and time of function execution start and end"""
    def wrapper():
        time_start = datetime.datetime.now()
        print('Started to use function at ', time_start)
        func()
        time_end = datetime.datetime.now()
        print('Finished to use function at ', time_end)
    return wrapper

def year_of_birth() -> tuple: #task 5.2
    """Output year of birth depending on the age in 2022"""
    y = tuple(map(lambda x: 2022-x, [18, 35, 72, 46, 13, 5, 27, 59]))
    print(y)

#task 5.3
@my_decorator 
def check_of_decorator():
    """Checks implementation of my decorator"""
    current_age = int(input('Please enter your age in current year: '))
    current_year = int(input('Kindly enter current year: '))
    your_year_of_birth = current_year-current_age 
    print('You was born in', your_year_of_birth)

 
#task 7.1.1
def all_burger_incredients(func) -> str: #decorator 7.1
    """Assists to output all burger incredients"""
    def other_burger_incredients():
        first_ingredient = 'булка'
        second_ingredient = 'салат'
        third_ingredient = 'помидоры'
        print(third_ingredient)
        func()
        print(second_ingredient)
        print(first_ingredient) 
    return other_burger_incredients

@all_burger_incredients
def main_burger_ingredient():
    """Adds main burger ingredient"""
    main_ingredient = 'котлета'
    print(main_ingredient)

#task 7.1.2
def show_function_name_and_arguments(func):
    """Decorator which shows function name and arguments"""
    def wrapper_2():
        argnames = func.__code__.co_varnames
        function_name = func.__name__
        print('Function name is', function_name)
        print('Function arguments are', argnames)
        func()
    return wrapper_2
        
@show_function_name_and_arguments    
def function_to_be_decorated():
    """Function name and arguments should be showed using decorator"""
    a = 2
    t = 6
    result = a+t
    print(result)


#task 7.1.3
def decorator_with_countdown(func):
    """Decorator which counts the time down"""
    def countdown():
        t = 5
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer)
            time.sleep(1)
            t -= 1
        func()
    return countdown

@decorator_with_countdown
def function_example():
    print ('Я просто функция')

#task 7.2.1
def round_values():
    """Rounds values and prints as a list"""
    values = [6.56773, 9.57668, 4.00914, 56.24241, 9.01344, 32.00013]
    rounded_values = list(map(round, values))
    print(rounded_values)

#task 7.2.2
def print_scores_over_80():
    """Prints scores over 80"""
    scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65, 92, 85]
    scores_over_80 = filter(lambda x: x>80, scores)
    print(list(scores_over_80))

#task 7.2.3
def find_palindromes():
    """Finds palindromes"""
    values = ["demigod", "rewire", "madam", "fortran", "python", "xamarin", "salas", "PHP"]
    palindromes = filter(lambda a: ''.join(reversed(a)) == a, values)
    print(list(palindromes))

#task 7.2.4
def multiply_values():
    """"Multiply values from the list"""
    values= [1, 2, 3, 4]
    result = reduce(lambda v, s: v*s, values)
    print(result)

#task 7.2.5
def return_maximum_value():
    """Choose maximum value from the list"""
    values=[3, 5, 2, 4, 7, 1] 
    maximum_value = reduce(max, values)
    print(maximum_value)

#task 7.2.6
def count_word_repeats():
    """Counts how many times the word appeared in the list"""
    sentences = ['капитан джек воробей', 'капитан дальнего плавания', 'ваша лодка готова, капитан']
    word_repeats = sum(map(lambda x : 1 if 'капитан' in x else 0, sentences))
    print(word_repeats)


if __name__ == '__main__':
    count_word_repeats()
