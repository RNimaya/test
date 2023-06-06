# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.

# Any code taken from other sources is referenced within my code solution.
# Student ID: w1959878

# Date: 6.12.2022

# This is Part 4 of the coursework which includes a dictionary to store UoW ID with results
# This program gets the UoW numbers as inputs when run and maps them to
# each of the results that were stored in the file in that specific order to a dictionary

# Declaring variables
progress_dict = {}


def get_uow_id():
    """Get UOW IDs and assign them to their progress result in the dictionary"""
    result_count = 1
    global progress_dict
    progress_dict = {}
    # Reading progress from File
    fo = open("progress_results.txt", "r")

    # This is used to read the file line by line and then get UoW id as input for each progress result
    for line in fo:
        valid_uow_id = uow_id_validation(result_count)
        result = line.strip("\n")
        # This is used to assign the UoW number to the progress result
        progress_dict[valid_uow_id] = result
        result_count += 1
    ask = input("If you want to view student ID and their results now enter y: ")
    ask=ask.lower()
    if ask in ("yes" or "y"):
        view_results_with_id()
    else:
        return
    fo.close()


def view_results_with_id():
    """This prints out all the uow ids with their results from the dictionary
    or if the dictionary is empty it will ask to enter UoW IDs"""
    global progress_dict
    if progress_dict != {}:
        print("""\nStudent ID and results""")
        for (k, v) in progress_dict.items():
            print(k, ":", v, end=" ")
        print("\n")

    else:  # If there are no values in the dictionary then the program will request the
        get_uow_id()  # uow IDs and will then display the results
    print("\n")


def uow_id_validation(result_count):
    """This checks whether the UoW ID entered
    is of the correct format eg: w12345678"""
    uow_id = input("Enter UoW ID for progress result " + str(result_count) + ":")
    if len(uow_id) == 8 and uow_id[0] == "w":
        if uow_id not in progress_dict:
            return uow_id
        else:
            print("UoW ID already exists")
            return uow_id_validation(result_count)
    else:
        print("Invalid Uow Number")
        return uow_id_validation(result_count)
