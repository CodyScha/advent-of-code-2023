import re

input = open("day2input.txt")
input_lines = input.readlines()

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

def part1():
    sum = 0

    for game in input_lines:
        game_impossible = False
        #* get the Game ID
        colon_split = game.split(':')
        game_id = re.search(r'\d+', colon_split[0]).group()

        #* now we need to parse and get the individual pulls
        semicolon_split = colon_split[1].split(';')

        for pull in semicolon_split:
            pull_impossible = False
            #* get the number of each color in the pull
            num_green = get_num_color_in_pull("green", pull)
            num_red = get_num_color_in_pull("red", pull)
            num_blue = get_num_color_in_pull("blue", pull)
            
            pull_impossible = num_green > MAX_GREEN or num_red > MAX_RED or num_blue > MAX_BLUE

            #* only one pull needs to be impossible to consider the
            #* game impossible
            game_impossible = game_impossible or pull_impossible
        
        if not game_impossible:
            sum = sum + int(game_id)

    return sum


def part2():
    sum = 0

    for game in input_lines:
        minimum_green = 0
        minimum_red = 0
        minimum_blue = 0
        power = 0

        colon_split = game.split(':')
        semicolon_split = colon_split[1].split(';')

        for pull in semicolon_split:
            num_green_in_pull = get_num_color_in_pull("green", pull)
            num_red_in_pull = get_num_color_in_pull("red", pull)
            num_blue_in_pull = get_num_color_in_pull("blue", pull)

            minimum_green = num_green_in_pull if num_green_in_pull > minimum_green else minimum_green
            minimum_red = num_red_in_pull if num_red_in_pull > minimum_red else minimum_red
            minimum_blue = num_blue_in_pull if num_blue_in_pull > minimum_blue else minimum_blue
        
        power = minimum_green * minimum_red * minimum_blue

        sum = sum + power

    return sum


def get_num_color_in_pull(color_str, pull):
    num_color = 0
    color_search = re.search(f'\\d+ {color_str}', pull)
    if color_search != None:
        num_color = int(re.search(r'\d+', color_search.group()).group())

    return num_color


print(part1())
print(part2())