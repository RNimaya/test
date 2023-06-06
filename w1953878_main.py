# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.

# Any code taken from other sources is referenced within my code solution.
# Student ID: w1959878

# Date: 2.12.2022
# importing modules
import dictionary

# Initializing variables
progress = 0
trailer = 0
retriever = 0
excluded = 0
outcome_list = []


# User defined functions
def progress_out(pass_credits, defer_credits, fail_credits):
    """This function is used to predict the outcomes based on the marks/credits"""
    global progress, trailer, retriever, excluded, outcome_list
    result = ""

    if pass_credits in (120, 100) and defer_credits in (0, 20) and fail_credits in (0, 20):
        if pass_credits == 120:
            result = "Progress"
            progress += 1

        else:
            result = "Progress (module trailer)"
            trailer += 1

    elif pass_credits in range(0, 81, 20) and defer_credits in range(0, 121, 20) and fail_credits in (60, 40, 20, 0):
        result = "Module Retriever"
        retriever += 1

    elif pass_credits in (40, 20, 0) and defer_credits in (40, 20, 0) and fail_credits in (120, 100, 80):
        result = "Exclude"
        excluded += 1

    # This is Part 2 of the coursework aka list extension
    # This code segment adds the result and the credits to the list
    outcome_list.append((result, pass_credits, defer_credits, fail_credits))
    print()
    print(result)


def input_validation(input_credits, mode):
    """Used to validate the marks input and carry out expected action"""
    if input_credits not in range(0, 121, 20):
        print("\nOut of Range")
        if mode == 1:
            return get_input()
        else:
            return get_input_staff()
    else:
        return True


def histogram(prog_count, trail_count, ret_count, excld_count):
    """This function is used to print the histogram of results in staff mode"""
    print("\n")
    print("-" * 50)
    print("Histogram")
    print(f"Progress {prog_count}\t: {'*' * prog_count}")
    print(f"Trailer {trail_count}\t: {'*' * trail_count}")
    print(f"Retriever {ret_count}\t: {'*' * ret_count}")
    print(f"Excluded {excld_count}\t: {'*' * excld_count}")
    print()

    tot_outcomes = prog_count + trail_count + ret_count + excld_count
    print(tot_outcomes, " outcomes in total")
    print("-" * 50)


def view_results_from_list():
    """This function is used to print all the values from the list"""
    global outcome_list
    print("\nThis is the output from the list")
    for i in outcome_list:
        out = f"{i[0]} - {i[1]},{i[2]},{i[3]}"
        print(out)
    print()


# This is part 3 of the cw requirement to store the progress data in a file
def file_write():
    """This function is used to write the progression data to a file"""
    global outcome_list
    file = open("progress_results.txt", "w")
    for items in outcome_list:
        line = f"{items[0]} - {items[1]},{items[2]},{items[3]}"
        file.write(line + "\n")
    file.close()


def file_output():
    """This function is used to print the data from the file"""
    file = open("progress_results.txt", "r")
    print("\nThis is the output from the file")
    for line in file:
        print(line.strip("\n"))
    file.close()


def menu():
    """This function is used to call the menu to view outputs from list, file and dictionary"""
    try:
        print("""\nExtra  Functions Menu
------------------------
    1. Show histogram
    2. Show output from list
    3. Show output from file
    4. Access Dictionary to save UoW IDs with their results
    5. View Results with UoW ID
    6. Quit program\n""")

        option = int(input("Please enter an option number:  "))

        if option == 1:
            histogram(progress, trailer, retriever, excluded)
            menu()
        elif option == 2:
            view_results_from_list()
            menu()
        elif option == 3:
            file_output()
            menu()
        elif option == 4:
            dictionary.get_uow_id()
            menu()
        elif option == 5:
            dictionary.view_results_with_id()
            menu()
        elif option == 6:
            print("The program will close now...")
            quit()
        else:
            print("Invalid Option")
            menu()
    except ValueError:
        print("Invalid Input. Integer required.")
        return menu()


def ask_pass_credits():
    """Fuction to validate the pass credits"""
    try:
        pass_credits = int(input("\nPlease enter your total PASS credits: "))
        if pass_credits not in range(0, 121, 20):
            print("\nOut of Range")
            return ask_pass_credits()
        else:
            return pass_credits
    except ValueError:
        print("\nInvalid Input. Integer required.")
        return ask_pass_credits()


def ask_defer_credits():
    """Fuction to validate the defer credits"""
    try:
        defer_credits = int(input("Please enter your total DEFER credits: "))
        if defer_credits not in range(0, 121, 20):
            print("\nOut of Range")
            return ask_defer_credits()
        else:
            return defer_credits
    except ValueError:
        print("\nInvalid Input. Integer required.")
        return ask_defer_credits()



def ask_fail_credits():
    """Fuction to validate the fail credits"""
    try:
        fail_credits = int(input("Please enter your total FAIL credits: "))
        if fail_credits not in range(0, 121, 20):
            print("\nOut of Range")
            return ask_fail_credits()
        else:
            return fail_credits
    except ValueError:
        print("Invalid Input. Integer required.")
        return ask_fail_credits()


def get_input_staff():
    """Gets the credits from staff and validates them"""
    try:
        pass_credits = ask_pass_credits()
        defer_credits = ask_defer_credits()
        fail_credits = ask_fail_credits()

        total_credits = (pass_credits + defer_credits + fail_credits)
        if total_credits != 120:
            print("\nTotal Incorrect")
            return ask_to_continue()
        else:
            # Calls the progress output function to calculate result
            progress_out(pass_credits, defer_credits, fail_credits)
            ask_to_continue()

    except ValueError:
        print("\nInteger required")
        get_input_staff()


def get_input():
    """Gets the credits as input from student"""
    try:
        pass_credits = int(input("\nPlease enter your credits at PASS: "))
        if input_validation(pass_credits, 1):
            defer_credits = int(input("Please enter your credits at DEFER: "))
            if input_validation(defer_credits, 1):
                fail_credits = int(input("Please enter your credits at FAIL: "))
                if input_validation(fail_credits, 1):
                    total_credits = (pass_credits + defer_credits + fail_credits)
                    if total_credits != 120:
                        print("\nTotal Incorrect")
                        return get_input()
                    else:
                        # Calls the progress output function to calculate result
                        return progress_out(pass_credits, defer_credits, fail_credits)
    except ValueError:
        print("\nInteger required")
        get_input()


def ask_to_continue():
    print("\nWould you like to enter another set of data?")
    cont = input("Enter 'y' to continue or 'q' to quit and view results: ")
    cont = cont.lower()
    if cont in ("y", "yes"):
        return get_input_staff()
    elif cont == "q":
        file_write()  # writes all inputs and results to the file
        menu()  # Calls the menu to do parts 2,3 and 4 of the coursework specification
    else:
        print("\nInvalid Option.")
        return ask_to_continue()


def main():
    """This function contains the main selection of student or staff"""
    mode = input("Enter 1 for student mode or 2 for staff mode: ")
    try:
        mode = int(mode)
        if mode == 1:
            get_input()
        elif mode == 2:
            get_input_staff()
        else:
            print("\nInvalid Option...Enter 1 or 2\n")
            main()
    except ValueError:
        print("\nInvalid Input..Try again.\n")
        main()


# Starting main program
main()
