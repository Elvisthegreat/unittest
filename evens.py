def even_number_of_evens(numbers):

    """
    Should Raise a TypeError if a list in not passed into the function
    error message: "A list was not passed into the function"
    if the list is empty it will return False
    if the number of even numbers is odd - return False
    if the numner of even numbers is even - return True
    """
    
    if isinstance(numbers, list):
        if numbers == []: # returns False if an empty list is passed in
            return False
        else:
            """
            count the number of even numbers in the list 
            and then check if that number itself is even
            """
            evens = 0
        for n in numbers:
            if n % 2 == 0:
                evens += 1
        
        if evens:
            return evens % 2 == 0
        else:
            return False
    else:
        raise TypeError("A list was not pass into the function")

if __name__ == 'main':
    print(even_number_of_evens(5))