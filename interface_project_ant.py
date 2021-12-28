from errors_project_ant import WrongProbabilityError
from program_project_ant import create_gif_from_images, interface


def main():
    """
    Main function of the program. Uses interface to communicate with user.
    Has three main options.
    """

    print("LANGTON'S ANT\n\
    1 - create white board with given size\n\
    2 - process Langton's ant with given black-white image\n\
    3 - create black-white board with given size and probability\
 of black pixel")
    exit_program = False
    while not exit_program:
        choice1 = input("Insert number: ")
        if choice1 == "1":
            probability = 0
            isExistingPicture = False
        elif choice1 == "2":
            probability = 0
            isExistingPicture = True
        elif choice1 == "3":
            probability = input("Insert probability of black pixel: ")
            try:
                probability = float(probability)
            except ValueError:
                raise WrongProbabilityError(probability)
            isExistingPicture = False
        else:
            print("-Wrong number-")
            continue
        interface(probability, isExistingPicture)
        choice2 = input("Make gif from images?\n1 - Yes\n2- No\n: ")
        if choice2 == "1":
            directory = "obrazy/"
            create_gif_from_images(directory)
        print("Results in directory 'obrazy'")
        exit_program = True


if __name__ == "__main__":
    main()
