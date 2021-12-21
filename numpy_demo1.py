# import numpy as np
# from PIL import Image
# from random import choice, randint


# class InvalidLocationError(Exception):
#     pass


# class WrongProbabilityError(Exception):
#     def __init__(self, probability_of_black_square) -> None:
#         super().__init__("Probability must be between 0 and 1")
#         self.probability_of_black_square = probability_of_black_square


# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)


# def board():
#     size = input("Insert board size as tuple: ")
#     height, width = size.split()
#     height = int(height)
#     width = int(width)
#     num_of_squares = height * width
#     board = np.arange(0, num_of_squares).reshape(height, width)
#     return board


# def white_board():
#     size2 = input("Insert board size as tuple: ")
#     height, width = size2.split()
#     height = int(height)
#     width = int(width)
#     array = np.zeros([height, width], dtype=np.uint8)
#     for i in range(width):
#         for j in range(height):
#             if (i % 2) == (j % 2):
#                 array[j, i] = 0
#             else:
#                 array[j, i] = 255
#     # image_demo = Image.fromarray(array)
#     # image_demo.save("image_demo.jpg")


# def interface():
#     size2 = input("Insert board size as tuple: ")
#     height, width = size2.split()
#     height = int(height)
#     width = int(width)
#     x, y = random_ant_location(height, width)
#     create_white_board(height, width, x, y)
#     steps = input("Insert number of steps: ")
#     steps = int(steps)
#     white_board_moves(x, y, steps)


# def create_white_board(height, width, x, y):
#     array = np.zeros([height, width, 3], dtype=np.uint8)
#     for i in range(width):
#         for j in range(height):
#             array[j, i] = WHITE
#     array[x, y] = (255, 128, 0)
#     image_demo = Image.fromarray(array)
#     image_demo.save("image_demo3.png")


# def white_board_moves(x, y, steps):
#     image = Image.open("image_demo3.png")
#     numpy_image = np.asarray(image)
#     ant = Ant(x, y, "up", WHITE)
#     for i in range(steps):
#         color = ant.get_square_color()
#         if color is WHITE:
#             ant.move_white()
#             numpy_image[x, y] = BLACK
#         else:
#             ant.move_black()
#             numpy_image[x, y] = WHITE
#         x1 = ant.get_x()
#         y1 = ant.get_y()
#         if WHITE in numpy_image[x1, y1]:
#             ant.set_square_color(WHITE)
#         else:
#             ant.set_square_color(BLACK)
#         numpy_image[x1, y1] = (255, 128, 0)
#         x = x1
#         y = y1
#         image_next = Image.fromarray(numpy_image)
#         image_next.save(f"image_board_{i}.png")


# def random_ant_location(height, width):
#     x = randint(0, height)
#     y = randint(0, width)
#     return (x, y)


# def random_color_square(probability_of_black_square):
#     if probability_of_black_square > 1 or probability_of_black_square < 0:
#         raise WrongProbabilityError(probability_of_black_square)
#     list_of_colors = []
#     number_of_black = round(probability_of_black_square * 100)
#     number_of_white = 100 - number_of_black
#     for i in range(0, number_of_black):
#         list_of_colors.append(BLACK)
#     for i in range(0, number_of_white):
#         list_of_colors.append(WHITE)
#     color = choice(list_of_colors)
#     return color


# def random_direction_ant(wrong_way):
#     ways = ["up", "down", "left", "right"]
#     ways = [way for way in ways if way not in wrong_way]
#     final_direction = choice(ways)
#     return final_direction


# class Ant:
#     def __init__(self, x, y, direction, square_color):
#         if not x or not y:
#             raise InvalidLocationError("Location is empty")
#         self._x = x
#         self._y = y
#         self._square_color = square_color
#         self._direction = direction if direction else "up"

#     def get_direction(self):
#         return self._direction

#     def get_x(self):
#         return self._x

#     def get_y(self):
#         return self._y

#     def set_x(self, new_x):
#         self._x = new_x

#     def set_y(self, new_y):
#         self._y = new_y

#     def set_direction(self, new_direction):
#         self._direction = new_direction

#     def get_square_color(self):
#         return self._square_color

#     def set_square_color(self, new_color):
#         self._square_color = new_color

#     def move_white(self):
#         if self.get_direction() == "up":
#             self.set_direction("left")
#             self.set_y(self._y - 1)
#         elif self.get_direction() == "left":
#             self.set_direction("down")
#             self.set_x(self._x + 1)
#         elif self.get_direction() == "down":
#             self.set_direction("right")
#             self.set_y(self._y + 1)
#         elif self.get_direction() == "right":
#             self.set_direction("up")
#             self.set_x(self._x - 1)

#     def move_black(self):
#         if self.get_direction() == "up":
#             self.set_direction("right")
#             self.set_y(self._y + 1)
#         elif self.get_direction() == "left":
#             self.set_direction("up")
#             self.set_x(self._x - 1)
#         elif self.get_direction() == "down":
#             self.set_direction("left")
#             self.set_y(self._y - 1)
#         elif self.get_direction() == "right":
#             self.set_direction("down")
#             self.set_x(self._x + 1)


# class Board:
#     def __init__(self, height, width):
#         self._height = height
#         self._width = width

#     def get_height(self):
#         return self._height

#     def get_width(self):
#         return self._width

#     def set_height(self, new_height):
#         self._height = new_height

#     def set_width(self, new_width):
#         self._width = new_width


# if __name__ == "__main__":
#     interface()
