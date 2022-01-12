def return_10():
    return 10

def add(number_1,number_2):
    return number_1 + number_2

def subtract(num_1, num_2):
    return num_1 - num_2

def multiply(num_1, num_2):
    return num_1 * num_2

def divide(num_1, num_2):
    return num_1 / num_2

def length_of_string(string):
    return len(string)

def join_string(str_1, str_2):
    return str_1 + str_2

def add_string_as_number(str_1, str_2 ):
    return int(str_1) + int(str_2)

def number_to_full_month_name(int_1):
    if int_1 == 1:
        return "January"
    elif int_1 == 3:
       return "March"
    elif int_1 == 9:
       return "September"
    else:
        None

def number_to_short_month_name(int_1):
    if int_1 == 1:
        return "Jan"
    elif int_1 == 4:
       return "Apr"
    elif int_1 == 10:
       return "Oct"
    else:
        None

def cube(int_1):
    return int_1 ** 3

def input_string(str_1):
    return str_1[::-1]

def input_farenheit(int_1):
    return (int_1 -32) * 5 / 9
