import imageio
import os
import numpy as np
from PIL import Image
from config_project_ant import BLACK, WHITE, directions
from classes_project_ant import Ant
from random_utils_project_ant import (
    random_ant_location,
    random_color_square,
    random_direction_ant
)
from errors_project_ant import (
    OversizedHopError,
    WrongBoardSizeError,
    WrongDimensionsError,
    InvalidNameError,
    EmptyNameError
)


def interface(probability, isExistingPicture):
    if not isExistingPicture:
        try:
            size2 = input("Insert board size as integers: ")
            height, width = size2.split()
            height = int(height)
            width = int(width)
        except ValueError:
            raise WrongBoardSizeError(size2)
        if height < 2 or width < 2:
            raise WrongDimensionsError(height, width)
        height = int(height)
        width = int(width)
        x, y = random_ant_location(height, width)
        name = create_board(height, width, x, y, probability)
    else:
        name = input("Insert full name of image file: ")
        x, y, height, width, savedimage = convert_image_to_board_with_ant(name)
        name = "obrazy/image_board_first_ex_picture.png"
    moves = input("Insert number of moves: ")
    moves = int(moves)
    hop = input("Enter every how many moves to save the picture: ")
    hop = int(hop)
    if hop > moves:
        raise OversizedHopError(hop)
    board_moves(height, width, x, y, moves, hop, name)


def create_board(height, width, x, y, probability):
    """
    Creates three dimensional array with given shape (height, width)
    filled with zeros. For each pixel draws either black or white
    color with given probability and assigns to it.
    For given ant location (x, y), it puts orange color in this pixel.
    """
    array = np.zeros([height, width, 3], dtype=np.uint8)
    for i in range(width):
        for j in range(height):
            color = random_color_square(probability)
            array[j, i] = color
    array[x, y] = (255, 128, 0)
    image_demo = Image.fromarray(array)
    image_demo.save("obrazy/image_board_0.png")
    return "obrazy/image_board_0.png"


def board_moves(height, width, x, y, moves, hop, name):
    image = Image.open(name)
    numpy_image = np.asarray(image)
    ant = Ant(x, y, directions[0], WHITE)
    for i in range(1, moves + 1):
        color = ant.get_pixel_color()
        if color is WHITE:
            numpy_image[x, y] = BLACK
        else:
            numpy_image[x, y] = WHITE
        ant.pivot()
        way = ant.get_direction()
        x_ant = ant.get_x()
        y_ant = ant.get_y()
        if (way == "left" or way == "up") and \
           (y_ant == 0 and x_ant == 0):
            random_way = random_direction_ant(["left", "up"])
            ant.set_direction(random_way)
        elif (way == "up" or way == "right") and \
             (x_ant == 0 and y_ant == width - 1):
            random_way = random_direction_ant(["right", "up"])
            ant.set_direction(random_way)
        elif (way == "down" or way == "right") and \
             (x_ant == height - 1 and y_ant == width - 1):
            random_way = random_direction_ant(["right", "down"])
            ant.set_direction(random_way)
        elif (way == "left" or way == "down") and \
             (x_ant == height - 1 and y_ant == 0):
            random_way = random_direction_ant(["left", "down"])
            ant.set_direction(random_way)
        elif way == "up" and x_ant == 0:
            random_way = random_direction_ant(["up"])
            ant.set_direction(random_way)
        elif way == "right" and y_ant == width - 1:
            random_way = random_direction_ant(["right"])
            ant.set_direction(random_way)
        elif way == "down" and x_ant == height - 1:
            random_way = random_direction_ant(["down"])
            ant.set_direction(random_way)
        elif way == "left" and y_ant == 0:
            random_way = random_direction_ant(["left"])
            ant.set_direction(random_way)
        ant.move_forward()
        x1 = ant.get_x()
        y1 = ant.get_y()
        if WHITE in numpy_image[x1, y1]:
            ant.set_pixel_color(WHITE)
        else:
            ant.set_pixel_color(BLACK)
        numpy_image[x1, y1] = (255, 128, 0)
        x = x1
        y = y1
        if i % hop == 0:
            image_next = Image.fromarray(numpy_image)
            image_next.save(f"obrazy/image_board_{i}.png")


def convert_image_to_board_with_ant(name):
    """
    Converts given png image into 3-dimensional array (RGB)
    and puts orange pixel(ant) in random pixel.
    Saves new image as image_board_first_ex_picture.png in
    directory obrazy. Returns size of new picture, location of ant
    and new image itself.
    """
    if not name:
        raise EmptyNameError("Image name cannot be empty")
    try:
        image_rgba = Image.open(name)
    except FileNotFoundError:
        raise InvalidNameError(name)
    image_rgb = image_rgba.convert("RGB")
    height_img, width_img = image_rgb.size
    numpy_img = np.asarray(image_rgb)
    x, y = random_ant_location(height_img, width_img)
    numpy_img[x, y] = (255, 128, 0)
    final_image = Image.fromarray(numpy_img)
    final_image.save("obrazy/image_board_0_from_mock.png")
    return (x, y, height_img, width_img, final_image)


def create_gif_from_images(directory_name):
    "NEED TO FIX FILE NAME READING. IT SORTS 0, 1, 10, 2, ...\
     instead of reading 0, 1, 2, 3 "
    images_list = []
    for image_file in sorted(os.listdir(directory_name)):
        file_path = os.path.join(directory_name, image_file)
        images_list.append(imageio.imread(file_path))
    imageio.mimsave("obrazy/ant_moves.gif", images_list, fps=2)
    return
