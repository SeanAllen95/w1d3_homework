def return_10():
    return 10

def add(first_number, second_number):
    return first_number + second_number

def subtract(num1, num2):
    return num1 - num2

def multiply(x, y):
    return x * y

def divide(a, b):
    return a / b

def length_of_string(test_string):
    return len(test_string)

def join_string(string_1, string_2):
    return string_1 +string_2

def add_string_as_number(str1, str2):
    a = int(str1)
    b = int(str2)
    result = a + b
    return result

def number_to_full_month_name(num):
    months = ["January",
              "February",
              "March",
              "April",
              "May",
              "June",
              "July",
              "August",
              "September",
              "October",
              "November",
              "December"]
    return months[num - 1]

def number_to_short_month_name(num):
    months = ["Jan",
              "Feb",
              "Mar",
              "Apr",
              "May",
              "Jun",
              "Jul",
              "Aug",
              "Sep",
              "Oct",
              "Nov",
              "Dec"]
    return months[num - 1]

#Further

def volume_of_cube(num):
    return num ** 3

def reverse_string(str1):
    new_str = str1[::-1]
    str(new_str)
    return new_str

def fahrenheit_to_celcius(far):
    result = (far - 32) * (5 / 9)
    return result


