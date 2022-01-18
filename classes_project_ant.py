from config_project_ant import BLACK, WHITE, directions


class EmptyPixelColorError(Exception):
    pass


class EmptyDirectionError(Exception):
    pass


class InvalidDirectionError(Exception):
    def __init__(self, direction) -> None:
        super().__init__("Direction not in directions list")
        self.direction = direction


class InvalidColorError(Exception):
    pass


class Ant:
    def __init__(self, x: int, y: int,  pixel_color: tuple, direction: str = "up"):
        """
        Class Ant. Contains attributes:
        :param x: ant's x (height) coordinate (location)
        :type x: int

        :param y: ant's y (width) coordinate (location)
        :type y: int

        :param direction: ant's direction, default to 'up'
        :type direction: str

        :param pixel_color: color of pixel where ant is in RGB mode,
        either WHITE (0, 0, 0) or BLACK (255, 255, 255)
        :type pixel_color: tuple
        """
        self._x = x
        self._y = y
        if not pixel_color:
            raise EmptyPixelColorError("Color cannot be empty")
        if pixel_color not in (WHITE, BLACK):
            raise InvalidColorError("Invalid color")
        self._pixel_color = pixel_color
        self._direction = direction

    def get_direction(self):
        return self._direction

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def set_x(self, new_x: int):
        self._x = new_x

    def set_y(self, new_y: int):
        self._y = new_y

    def set_direction(self, new_direction: str):
        if not new_direction:
            raise EmptyDirectionError("Direction is empty")
        if new_direction not in directions:
            raise InvalidDirectionError(new_direction)
        self._direction = new_direction

    def get_pixel_color(self):
        return self._pixel_color

    def set_pixel_color(self, new_color):
        if not new_color:
            raise EmptyPixelColorError("Color cannot be empty")
        self._pixel_color = new_color

    def pivot(self):
        """
        Turns ant ninety degree left or right depending on
        which pixel color it stands.
        """
        color = self.get_pixel_color()
        if color is not WHITE and color is not BLACK:
            raise InvalidColorError("Invalid color")
        if color is WHITE:
            shift_dir = 3
        else:
            shift_dir = 1
        current_direction = directions.index(self.get_direction())
        direction = (current_direction + shift_dir) % 4
        self.set_direction(directions[direction])

    def move_forward(self):
        """
        Moves ant one step forward in AxB board depending on direction.
        """
        if self.get_direction() == "up":
            self.set_x(self._x - 1)
        elif self.get_direction() == "left":
            self.set_y(self._y - 1)
        elif self.get_direction() == "down":
            self.set_x(self._x + 1)
        else:
            self.set_y(self._y + 1)
