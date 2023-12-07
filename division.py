# try except block - try catch block

class NegativeError(Exception):
    pass
    

try:
    n = int(input("Enter a numerator: "))
    d = int(input("Enter a denominator: "))

    if n < 0 or d < 0:
        raise NegativeError("No Negative numbers please")


    q = n / d 

    print(q)

except ZeroDivisionError:
    print("Denominator cannot be zero")

except ValueError: 
    print("Please type numbers only")

except NegativeError:
    print("No Negative numbers please")

except Exception as e: 
    print(e)
    print("Something went wrong")

else: 
    # Whenever try block is successfully executed without throwing any exceptions
    print("I am else block")

finally: 
    # This will run at the end whether any error was thrown or not
    print("Finally it has happened to me - I'm the block")

print("End of the program")

# file handling example

# try:
    # open a file 
    # try to do something 
    # write into file - it may throw error
# except: 
    # handle the error 
# finally block: 
    # close the file



