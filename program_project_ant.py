import imageio
import os
import numpy as np
from PIL import Image
from config_project_ant import (
    BLACK,
    WHITE,
    directions
)
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
    EmptyNameError,
    IncorrectImageColorsError,
    IncorrectTypeError
)


def interface(probability, isExistingPicture):
    """
    Proceeds main() function by choosing to create new board with
    given probability of black pixel if user chose to create board or
    transform external image to Langton's ant board.
    """
    directory = "obrazy"
    if not isExistingPicture:
        try:
            size2 = input("Insert board size as integers: ")
            height, width = size2.split()
            height = int(height)
            width = int(width)
        except ValueError:
            raise WrongBoardSizeError(size2)
        check_if_wrong_board_size(height, width)
        x, y = random_ant_location(height, width)
        name, st_color = create_board(height, width, x, y, probability, directory)
    else:
        name = input("Insert full name of image file \
(Attention: Use 'image_mock.png' as sample): ")
        temp = convert_image_to_board_with_ant(name, directory)
        x, y, height, width, saved_picture = temp
        name = f"{directory}/0.png"
    moves = input("Insert number of moves: ")
    hop = input("Enter every how many moves to save the picture: ")
    try:
        moves = int(moves)
        hop = int(hop)
    except ValueError:
        raise IncorrectTypeError(hop)
    check_if_too_big_hop(moves, hop)
    board_moves(height, width, x, y, moves, hop, name, directory, st_color)


def create_board(height, width, x, y, probability, directory):
    """
    Creates three dimensional array with given shape (height, width)
    filled with zeros. For each pixel draws either black or white
    color with given probability and assigns to it.
    For given ant location (x, y), it puts orange color in this pixel.
    Saves image in directory.
    """
    starting_color = WHITE
    array = np.zeros([height, width, 3], dtype=np.uint8)
    for i in range(width):
        for j in range(height):
            color = random_color_square(probability)
            array[j, i] = color
            if (j, i) == (x, y):
                starting_color = color
    array[x, y] = (255, 128, 0)
    image_demo = Image.fromarray(array)
    image_demo.save(f"{directory}/0.png")
    return f"{directory}/0.png", starting_color


def board_moves(height, width, x, y, moves, hop, name, directory, st_color):
    """
    Controls movement of Ant and colors of pixels on board in image file.
    When Ant is about to cross the borders of an image, it chooses
    random different direction. Saves image in directory for every hop.
    """
    image = Image.open(name)
    numpy_image = np.asarray(image)
    ant = Ant(x, y, st_color, directions[0])
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
        random_way = way
        if (way == "left" or way == "up") and \
           (y_ant == 0 and x_ant == 0):
            random_way = random_direction_ant(["left", "up"])
        elif (way == "up" or way == "right") and \
             (x_ant == 0 and y_ant == width - 1):
            random_way = random_direction_ant(["right", "up"])
        elif (way == "down" or way == "right") and \
             (x_ant == height - 1 and y_ant == width - 1):
            random_way = random_direction_ant(["right", "down"])
        elif (way == "left" or way == "down") and \
             (x_ant == height - 1 and y_ant == 0):
            random_way = random_direction_ant(["left", "down"])
        elif way == "up" and x_ant == 0:
            random_way = random_direction_ant(["up"])
        elif way == "right" and y_ant == width - 1:
            random_way = random_direction_ant(["right"])
        elif way == "down" and x_ant == height - 1:
            random_way = random_direction_ant(["down"])
        elif way == "left" and y_ant == 0:
            random_way = random_direction_ant(["left"])
        ant.set_direction(random_way)
        ant.move_forward()
        x_after_move = ant.get_x()
        y_after_move = ant.get_y()
        if WHITE in numpy_image[x_after_move, y_after_move]:
            ant.set_pixel_color(WHITE)
        else:
            ant.set_pixel_color(BLACK)
        numpy_image[x_after_move, y_after_move] = (255, 128, 0)
        x = x_after_move
        y = y_after_move
        if i % hop == 0:
            image_next = Image.fromarray(numpy_image)
            image_next.save(f"{directory}/{i}.png")


def convert_image_to_board_with_ant(name, directory):
    """
    Converts given png image into 3-dimensional array (RGB)
    and puts orange pixel(ant) on random pixel.
    Use 'image_mock.png' as sample image.
    Saves new image as 0.png in given obrazy.
    Returns size of new picture, location of ant and new image itself.
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
    w, b, othe = count_number_of_color_pixels(height_img, width_img, image_rgb)
    if othe > 0:
        raise IncorrectImageColorsError(othe)
    x, y = random_ant_location(height_img, width_img)
    numpy_img[x, y] = (255, 128, 0)
    final_image = Image.fromarray(numpy_img)
    final_image.save(f"{directory}/0.png")
    return (x, y, height_img, width_img, final_image)


def count_number_of_color_pixels(height, width, image):
    """
    Returns number of white, black and other color pixels as tuple.
    """
    white_pixels = 0
    black_pixels = 0
    other_colors_pixels = 0
    for i in range(height):
        for j in range(width):
            if image.getpixel((i, j)) == WHITE:
                white_pixels += 1
            elif image.getpixel((i, j)) == BLACK:
                black_pixels += 1
            else:
                other_colors_pixels += 1
    return (white_pixels, black_pixels, other_colors_pixels)


def create_gif_from_images(dir_name, ips):
    """
    Creates gif file from png images in given directory
    with given speed (ips - images per second).
    """
    images_list = []
    for image_file in sorted(os.listdir(dir_name), key=lambda x: int(x[:-4])):
        file_path = os.path.join(dir_name, image_file)
        images_list.append(imageio.imread(file_path))
    imageio.mimsave(f"{dir_name}/ant_moves.gif", images_list, fps=ips)
    return


def delete_all_image_files_in_dir():
    """
    Removes all files from 'obrazy' directory.
    """
    directory = "obrazy"
    for file_image in os.listdir(directory):
        os.remove(os.path.join(directory, file_image))
    return


def check_if_wrong_board_size(height, width):
    if height < 2 or width < 2:
        raise WrongDimensionsError(height, width)
    return


def check_if_too_big_hop(moves, hop):
    if hop > moves:
        raise OversizedHopError(hop)
    return
