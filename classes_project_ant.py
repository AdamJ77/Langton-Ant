from config_project_ant import WHITE, directions


class InvalidLocationError(Exception):
    pass


class EmptyPixelColorError(Exception):
    pass


class EmptyDirectionError(Exception):
    pass


class Ant:
    def __init__(self, x, y, direction, pixel_color):
        # if not x or not y:
        #     raise InvalidLocationError("Location is empty"
        self._x = x
        self._y = y
        if not pixel_color:
            raise EmptyPixelColorError("Color cannot be empty")
        self._pixel_color = pixel_color
        self._direction = direction if direction else "up"

    def get_direction(self):
        return self._direction

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def set_x(self, new_x):
        # if not new_x:
        #     raise InvalidLocationError("Location is empty")
        self._x = new_x

    def set_y(self, new_y):
        # if not new_y:
        #     raise InvalidLocationError("Location is empty")
        self._y = new_y

    def set_direction(self, new_direction):
        if not new_direction:
            raise EmptyDirectionError("Direction is empty")
        self._direction = new_direction

    def get_pixel_color(self):
        return self._pixel_color

    def set_pixel_color(self, new_color):
        if not new_color:
            raise EmptyPixelColorError("Color cannot be empty")
        self._pixel_color = new_color

    def pivot(self, color):
        if not color:
            raise EmptyPixelColorError("Color cannot be empty")
        if color is WHITE:
            shift_dir = 3
        else:
            shift_dir = 1
        current_direction = directions.index(self.get_direction())
        direction = (current_direction + shift_dir) % 4
        self.set_direction(directions[direction])

    def move_forward(self):
        if self.get_direction() == "up":
            self.set_x(self._x - 1)
        elif self.get_direction() == "left":
            self.set_y(self._y - 1)
        elif self.get_direction() == "down":
            self.set_x(self._x + 1)
        else:
            self.set_y(self._y + 1)
