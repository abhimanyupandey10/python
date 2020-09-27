# This program prints the table of the number entered ,using 2 functions.

# This function asks the value to the user that which table to print.


def get_number ():
    number = int(input('Enter a number: '))
    return number

def get_limit():
	limit = int(input('Enter the limit of the table: '))
	return limit

# The second function does the main thing, it prints the multiplication of the number entered.
def print_table (number):
    for i in range (1,11):
        print(number , 'x' , i , '=' , number * i)

number = get_number()
print_table(number)