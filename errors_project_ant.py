class WrongProbabilityError(Exception):
    def __init__(self, probability_of_black_square):
        super().__init__("Probability must be number between 0 and 1")
        self.probability_of_black_square = probability_of_black_square


class WrongDimensionsError(Exception):
    def __init__(self, height, width) -> None:
        super().__init__("Dimensions must be integers greater than 2.")
        self.height = height
        self.width = width


class WrongBoardSizeError(Exception):
    def __init__(self, size2) -> None:
        super().__init__("Board size must be positive integers greater than 1")
        self.size2 = size2


class InvalidNameError(Exception):
    def __init__(self, name) -> None:
        super().__init__("Did not found the name. Must be extension PNG.")
        self.name = name


class OversizedHopError(Exception):
    def __init__(self, hop) -> None:
        super().__init__("Hop is too great. No picture will be created.")
        self.hop = hop


class EmptyNameError(Exception):
    pass
