from random import choice, randint
from config_project_ant import BLACK, WHITE, directions
from errors_project_ant import WrongProbabilityError, WrongDimensionsError


def random_ant_location(height, width):
    """
    Chooses random tuple of integers that are representing ant location
    in two-dimensional board.
    """
    if height < 0 or width < 0:
        raise WrongDimensionsError(height, width)
    x = randint(0, height - 1)
    y = randint(0, width - 1)
    return (x, y)


def random_color_square(probability_of_black_square):
    """
    Chooses black or white color with given probability of black occurence.
    """
    if probability_of_black_square > 1 or probability_of_black_square < 0:
        raise WrongProbabilityError(probability_of_black_square)
    list_of_colors = []
    number_of_black = round(probability_of_black_square * 100)
    number_of_white = 100 - number_of_black
    for i in range(0, number_of_black):
        list_of_colors.append(BLACK)
    for i in range(0, number_of_white):
        list_of_colors.append(WHITE)
    color = choice(list_of_colors)
    return color


def random_direction_ant(wrong_ways):
    """
    Chooses randomly one way from list of directions that
    are not in given wrong directions.
    """
    correct_ways = [way for way in directions if way not in wrong_ways]
    final_direction = choice(correct_ways)
    return final_direction
