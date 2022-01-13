from errors_project_ant import WrongProbabilityError
from program_project_ant import (
    create_gif_from_images,
    interface,
    delete_all_image_files_in_dir)


def main():
    """
    Main function of the program. Uses interface to communicate with user.
    Has four main options.
    """

    print("LANGTON'S ANT\n\
1 - create white board with given size\n\
2 - process Langton's ant with given black-white image\n\
3 - create black-white board with given size and probability\
 of black pixel\n\
4 - delete all image files from directory 'obrazy'")
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
        elif choice1 == "4":
            delete_all_image_files_in_dir()
            continue
        else:
            print("-Wrong number-")
            continue
        interface(probability, isExistingPicture)
        if_gif = input("Make gif from images?\n1 - Yes\n2 - No\n: ")
        if if_gif == "1":
            images_per_sec = input("Insert number of images per sec in gif: ")
            directory = "obrazy/"
            create_gif_from_images(directory, images_per_sec)
        print("Results in directory 'obrazy'")
        exit_program = True


if __name__ == "__main__":
    main()
