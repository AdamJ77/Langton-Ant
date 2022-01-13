from classes_project_ant import Ant
from classes_project_ant import (
    EmptyDirectionError,
    EmptyPixelColorError,
    InvalidColorError,
    InvalidDirectionError,
)
from errors_project_ant import (
    WrongDimensionsError,
    WrongBoardSizeError,
    InvalidNameError,
    OversizedHopError,
    EmptyNameError,
    WrongProbabilityError
)
from config_project_ant import BLACK, WHITE
from program_project_ant import (
    convert_image_to_board_with_ant,
    create_board,
    interface,
    count_number_of_color_pixels
)
from random_utils_project_ant import (
    random_ant_location,
    random_color_square,
    random_direction_ant
)
import pytest
from PIL import Image
import numpy as np


def test_ant():
    ant = Ant(5, 6, "up", BLACK)
    assert ant.get_x() == 5
    assert ant.get_y() == 6
    assert ant.get_direction() == "up"
    assert ant.get_pixel_color() == BLACK


def test_ant_new():
    ant = Ant(5, 6, "up", BLACK)
    assert ant.get_x() == 5
    assert ant.get_y() == 6
    assert ant.get_direction() == "up"
    assert ant.get_pixel_color() == BLACK
    ant.set_direction("down")
    ant.set_x(10)
    ant.set_y(15)
    ant.set_pixel_color(WHITE)
    assert ant.get_x() == 10
    assert ant.get_y() == 15
    assert ant.get_direction() == "down"
    assert ant.get_pixel_color() == WHITE


def test_invalid_direction_ant():
    ant = Ant(5, 6, "up", BLACK)
    with pytest.raises(InvalidDirectionError):
        ant.set_direction("-1")
    with pytest.raises(EmptyDirectionError):
        ant.set_direction("")


def test_invalid_pixel_color():
    with pytest.raises(InvalidColorError):
        Ant(4, 6, "up", 2)
    with pytest.raises(EmptyPixelColorError):
        Ant(4, 7, "right", ())


def test_ant_pivot():
    ant1 = Ant(5, 6, "up", BLACK)
    ant2 = Ant(10, 24, "left", WHITE)
    ant1.pivot()
    ant2.pivot()
    assert ant1.get_direction() == "right"
    assert ant2.get_direction() == "down"


def test_ant_move_forward():
    ant1 = Ant(10, 10, "up", BLACK)
    ant2 = Ant(10, 10, "left", WHITE)
    ant3 = Ant(10, 10, "right", WHITE)
    ant4 = Ant(10, 10, "down", BLACK)
    ant1.move_forward()
    ant2.move_forward()
    ant3.move_forward()
    ant4.move_forward()
    assert ant1.get_x() == 9 and ant1.get_y() == 10
    assert ant2.get_x() == 10 and ant2.get_y() == 9
    assert ant3.get_x() == 10 and ant3.get_y() == 11
    assert ant4.get_x() == 11 and ant4.get_y() == 10


def test_random_ant_location(monkeypatch):
    def returx(a, b):
        return 5
    monkeypatch.setattr("random_utils_project_ant.randint", returx)
    x, y = random_ant_location(10, 10)
    assert x == 5 and y == 5


def test_random_ant_location_error():
    with pytest.raises(WrongDimensionsError):
        random_ant_location(-1, 10)


def test_random_color_square_black_white_certain():
    color1 = random_color_square(1)
    color2 = random_color_square(0)
    assert color1 == BLACK
    assert color2 == WHITE


def test_random_color_square(monkeypatch):
    def returnBlack(a):
        return BLACK
    monkeypatch.setattr("random_utils_project_ant.choice", returnBlack)
    color = random_color_square(0.5)
    assert color == BLACK


def test_random_color_square_invalid_probability():
    with pytest.raises(WrongProbabilityError):
        random_color_square(1.5)
        random_color_square(-1)


def test_random_direction_ant(monkeypatch):
    def returnLeft(b):
        return "left"
    monkeypatch.setattr("random_utils_project_ant.choice", returnLeft)
    wrong_ways = ["up", "down"]
    result_way = random_direction_ant(wrong_ways)
    assert result_way == "left"


def test_convert_image_to_board_with_ant_wrong_name():
    """
    Correct image name is:image_mock.png
    """
    directory = "test_obrazy"
    with pytest.raises(InvalidNameError):
        convert_image_to_board_with_ant("image1_test.png", directory)
    with pytest.raises(EmptyNameError):
        convert_image_to_board_with_ant("", directory)


def test_convert_image_to_board_with_ant(monkeypatch):
    """
    Testing image param:
    name: image_mock_test.png
    size: 100 x 100 pixels
    pixel colors: black and white
    """
    image_test = Image.open("test_obrazy/image_mock_test.png")
    image_test1 = image_test.convert("RGB")
    height, width = image_test1.size
    assert height == 100 and width == 100

    "CALCULATING NUMBER OF BLACK AND WHITE PIXELS"
    number_of_white_pixels, number_of_black_pixels, other = count_number_of_color_pixels(height, width, image_test1)
    assert number_of_black_pixels == 4954
    assert number_of_white_pixels == 5046
    assert other == 0
    """
    KNOWING NUMBER OF BLACK AND WHITE PIXELS FUNCTION WILL
    CHANGE ONE PIXEL (monkeypatch - BLACK) SO NUMBER OF BLACK
    PIXELS WILL DECREASE BY ONE AND WHITE WILL STAY THE SAME
    """
    """
    Testing pixel param:
    location: (0, 0) [left, top corner]
    color: black
    """
    pixel_color = image_test1.getpixel((0, 0))
    assert pixel_color == BLACK
    assert pixel_color != WHITE
    """
    New image:
    name: saved_picture
    """
    def returnspecificpixel(a, b):
        return (0, 0)
    monkeypatch.setattr("program_project_ant.random_ant_location", returnspecificpixel)
    directory = "test_obrazy"
    x, y, height1, width1, saved_picture = convert_image_to_board_with_ant("image_mock.png", directory)
    white_pixels, black_pixels, other_colors_pixels = count_number_of_color_pixels(height1, width1, saved_picture)
    assert x == 0 and y == 0
    assert height1 == 100 and width1 == 100
    assert white_pixels == 5046
    assert black_pixels == 4954 - 1
    assert other_colors_pixels == 1
    """
    In directory obrazy new image was created. Ant(orange pixel)
    is located in top left corner.
    """


def test_create_board_with_all_black():
    height = 50
    width = 50
    all_pixels = height * width
    probability = 1
    x = 20
    y = 25
    directory = "test_obrazy"
    image = create_board(height, width, x, y, probability, directory)
    image1 = Image.open(image)
    white_pixels, black_pixels, others_pixel = count_number_of_color_pixels(height, width, image1)
    assert black_pixels == 2499
    assert white_pixels == 0
    assert others_pixel == 1
    assert all_pixels == black_pixels + white_pixels + others_pixel


def test_create_board_with_all_white():
    height = 50
    width = 50
    all_pixels = height * width
    probability = 0
    x = 20
    y = 25
    directory = "test_obrazy"
    image = create_board(height, width, x, y, probability, directory)
    image1 = Image.open(image)
    white_pixels, black_pixels, others_pixel = count_number_of_color_pixels(height, width, image1)
    assert black_pixels == 0
    assert white_pixels == 2499
    assert others_pixel == 1
    assert all_pixels == black_pixels + white_pixels + others_pixel


def test_board_moves():
    # height = 50
    # width = 50
    # x = 20
    # y = 25
    # moves = 3
    # hop = 1
    # name = "test_image_board_moves.png"
    # directory = "test_obrazy"
    pass
