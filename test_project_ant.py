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
from program_project_ant import convert_image_to_board_with_ant, interface
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
    with pytest.raises(InvalidNameError):
        convert_image_to_board_with_ant("image1_test.png")
    with pytest.raises(EmptyNameError):
        convert_image_to_board_with_ant("")


def test_convert_image_to_board_with_ant(monkeypatch):
    """
    Testing image param:
    name: image_mock.png
    size: 100 x 100 pixels
    pixel colors: black and white
    """
    image_test = Image.open("image_mock.png")
    image_test1 = image_test.convert("RGB")
    height, width = image_test1.size
    assert height == 100 and width == 100

    "CALCULATING NUMBER OF BLACK AND WHITE PIXELS"
    number_of_white_pixels = 0
    number_of_black_pixels = 0
    for i in range(100):
        for j in range(100):
            if image_test1.getpixel((i, j)) == WHITE:
                number_of_white_pixels += 1
            else:
                number_of_black_pixels += 1
    assert number_of_black_pixels == 4954
    assert number_of_white_pixels == 5046
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
    """
    New image:
    name: saved_picture
    """
    def returnspecificpixel(a, b):
        return (0, 0)
    monkeypatch.setattr("program_project_ant.random_ant_location", returnspecificpixel)
    x, y, height, width, saved_picture = convert_image_to_board_with_ant("image_mock.png")
    white_pixels = 0
    black_pixels = 0
    other_color = 0
    for i in range(100):
        for j in range(100):
            if saved_picture.getpixel((i, j)) == WHITE:
                white_pixels += 1
            elif saved_picture.getpixel((i, j)) == BLACK:
                black_pixels += 1
            else:
                other_color += 1
    assert x == 0 and y == 0
    assert height == 100 and width == 100
    assert white_pixels == 5046
    assert black_pixels == 4954 - 1
    assert other_color == 1
    """
    In directory obrazy new image was created. Ant(orange pixel)
    is located in top left corner.
    """


def test_create_board_probability_black():
    pass


def test_create_board_probability_white():
    pass
