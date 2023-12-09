import re

num_literals = ["zero", "one", "two", "three", 
                "four", "five", "six", 
                "seven", "eight", "nine"]

input = open("day1input.txt")
input_lines = input.readlines()


def part1():
    sum = 0
    for line in input_lines:
        reverse_line = line[::-1]

        first_num = str(re.search(r'\d', line).group())
        second_num = str(re.search(r'\d', reverse_line).group())

        sum = sum + int(first_num + second_num)

    return sum

def part2():
    sum = 0
    for line in input_lines:
        reverse_line = line[::-1]
        first_num = ""
        second_num = ""

        first_num_digit = str(re.search(r'\d', line).group())
        first_num_digit_index = line.index(first_num_digit)
        first_literal_info = find_first_literal(line)
        
        if first_num_digit_index < first_literal_info[0]:
            first_num = first_num_digit
        else:
            first_num = str(num_literals.index(first_literal_info[1]))

        second_num_digit = str(re.search(r'\d', reverse_line).group())
        second_num_digit_index = line.rfind(second_num_digit)
        second_literal_info = find_last_literal(line)

        if second_num_digit_index > second_literal_info[0]:
            second_num = second_num_digit
        else:
            second_num = str(num_literals.index(second_literal_info[1]))

        sum = sum + int(first_num + second_num)

    return sum

def find_first_literal(line):
    first_index = len(line)
    first_literal = ""
    for num in num_literals:
        try:
            index = line.index(num)
        except ValueError as ve:
            index = len(line)
        
        if index < first_index:
            first_index = index
            first_literal = num
    
    return (first_index, first_literal)

def find_last_literal(line):
    last_index = -1
    last_literal = ""
    for num in num_literals:
        index = line.rfind(num)
        
        if index > last_index:
            last_index = index
            last_literal = num
    
    return (last_index, last_literal)


print(part1())
print(part2())