def iterator_basics():
    countries = ('Russia', 'USA', 'UK', 'Germany', 'France')
    countries_iter = iter(countries)

    print('Logic under the hood\n')
    
    while True:
        try:
            country = next(countries_iter)
        except StopIteration:
            break
        else:
            print(country)
    
    print('Iterating through the countries list :')

    for country in countries_iter:
        print(country) # No output because iterator is exhausted

    for country in countries:
        print(country)

def iterator_vs_iterable():
    '''
    An Iteratable is an object that can provide you with an iterator
    An Iterator is an object that allows you to iterate over it, and has a next() method that returns the next item in the sequence.
    '''
    countries = ('Russia', 'USA', 'UK', 'Germany', 'France')
    countries_iter = iter(countries)

    print("countries is a ",type(countries)) # <class 'tuple'> Which is iterable
    print("countries_iter is a ",type(countries_iter)) # <class 'tuple_iterator'> Which is an iterator

    print("next(countries_iter): ")
    print(next(countries_iter)) # Prints Russia

    print("iter_copy = iter(countries_iter)")
    iter_copy = iter(countries_iter)
    print("next(iter_copy): ")
    print(next(iter_copy)) # Prints USA. Reason: iter_copy is copy of same iterator object countries_iter.

    print("iter_copy_2 = iter(countries)")
    iter_copy_2 = iter(countries)
    print("next(iter_copy_2): ")
    print(next(iter_copy_2)) # Prints Russia again. Reason: iter_copy_2 is a new iterator object created from iterable countries.
    # Thus iterables allow you to restart iteration over them, but iterators do not.

def iterator_usage_with_sentinal_value():
    ''' 
    A sentinel value is used as a signal that there are no more items available.
    For example, when reading lines from a file until EOF (end-of-file), we use sentinel value None or empty string '' to indicate end of input.
    We will be creating iterator from a callable with sentinal value using iter(callable,sentinel). 
    '''

    with open('countries.txt') as file:
        print(file.readline(), end='') # This prints first line of countries.txt
        for line in iter(file.readline,''):
            print(line,end = '') # This reads all remaining lines of countries.txt
        print("\nNote the type is callable iterator : ", type(iter(file.readline,'')))
        
        try:
            print(next(iter(file.readline,''))) # This prints nothing since iterator is exhausted
        except StopIteration:
            print("This errored out because it does not create a new iterator")
            print("To create a new iterator, re-open the file and call iter(file.readline,'')")

    # Note that iter(file.readline, '') creates an iterator that calls file.readline() repeatedly until it returns ''
    # This pattern in Python allows you to create an iterator from a callable (in this case, the file.readline method) with a sentinel value. 

def main():
    # iterator_basics()
    # iterator_vs_iterable()
    iterator_usage_with_sentinal_value()



main()