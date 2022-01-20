from errors_project_ant import WrongProbabilityError
from program_project_ant import (
    create_gif_from_images,
    interface,
    delete_all_image_files_in_dir)


def main():
    """
    Main function of the program. Uses interface to communicate with user.
    Has three main options. Deletes all files in directory 'obrazy' before
    creating new ones.
    """

    print("LANGTON'S ANT\n\
1 - create white board with given size\n\
2 - transform black-white image to Langton's ant board\n\
3 - create black-white board with given size and probability\
 of black pixel\nPROGRAM DELETES ALL PREVIOUS IMAGE FILES BEFORE RUNNING")
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
        delete_all_image_files_in_dir()
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
