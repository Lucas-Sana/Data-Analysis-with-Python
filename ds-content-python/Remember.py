# Exercise 1
revenue_as_string = "500000"
revenue_as_integer = int(revenue_as_string)
revenue_as_integer


# Exercise 2

def func(x, y):
    return 2*x + y

func(10, 5)
func(-3, 10)


# Exercise 3

def last_letter(string):
    return string[-1]

last_letter('Python')
last_letter('RMOTR')


# Exercise 4

def list_size(my_list):
    size = len(my_list)
    
    if (size > 0):
        return 'List has {} elements'.format(size)
    else:
        return 'Error, no elements'

list_size([1, 2, 3])
list_size([])
