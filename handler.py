import sys
import os


def create_dict_of_sizes(root_folder, ext):
    dict_of_sizes = {}
    for root, dirs, files in os.walk(root_folder):
        for name in files:
            if os.path.splitext(name)[1] == "." + ext:
                size = os.path.getsize(os.path.join(root, name))
                if size not in dict_of_sizes:
                    dict_of_sizes[size] = [os.path.join(root, name)]
                else:
                    dict_of_sizes[size].append(os.path.join(root, name))
            elif not ext:  # if ext is not specified create dict of all files
                size = os.path.getsize(os.path.join(root, name))
                if size not in dict_of_sizes:
                    dict_of_sizes[size] = [os.path.join(root, name)]
                else:
                    dict_of_sizes[size].append(os.path.join(root, name))
    return dict_of_sizes


def print_sorted(dict_to_print, sort_option):
    if sort_option == 1:
        bool_reverse = True
    else:
        bool_reverse = False
    for key in sorted(dict_to_print.items(), reverse=bool_reverse):
        if len(key[1]) > 1:
            print(str(key[0]) + " bytes")
            print("\n".join(key[1]))


def main():
    sorting_options = [1, 2]
    root_folder = ""
    args = sys.argv
    try:
        root_folder = args[1]
    except IndexError:
        print("Directory is not specified")
    ext = input("Enter file format:\n ")
    print("Size sorting options:\n1. Descending\n2. Ascending\n")
    sorting_option = input("Enter a sorting option (1 or 2):\n")
    while int(sorting_option) not in sorting_options:
        print("Wrong option")
        sorting_option = input("Enter a sorting option (1 or 2):\n")

    dict_of_sizes = create_dict_of_sizes(root_folder, ext)
    print_sorted(dict_of_sizes, sorting_option)


if __name__ == "__main__":
    main()

