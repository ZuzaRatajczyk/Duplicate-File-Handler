import sys
import os


def flipp_dict(init_dict):
    flipped = {}
    for key, value in init_dict.items():
        if value not in flipped:
            flipped[value] = [key]
        else:
            flipped[value].append(key)
    return flipped


def check_num_of_val(dict_of_files):
    dict_to_print = {}
    for key, val in dict_of_files.items():
        if len(val) > 1:
            dict_to_print[key] = val
    return dict_to_print


def print_sorted(dict_to_print, sort_option):
    if int(sort_option) == 1:
        sort_keys = sorted(dict_to_print, reverse=True)
    else:
        sort_keys = sorted(dict_to_print)
    for key in sort_keys:
        print(str(key) + " bytes")
        print("\n".join(dict_to_print[key]))


def main():
    args = sys.argv
    try:
        root_folder = args[1]
    except IndexError:
        print("Directory is not specified")

    ext = input("Enter file format:\n ")
    options = [1, 2]
    dict_of_sizes = {}
    print("Size sorting options:\n1. Descending\n2. Ascending\n")
    sorting_option = input("Enter a sorting option:\n")
    while int(sorting_option) not in options:
        print("Wrong option")
        sorting_option = input("Enter a sorting option:\n")

    for root, dirs, files in os.walk(root_folder):
        for name in files:
            if os.path.splitext(name)[1] == "." + ext:
                dict_of_sizes[os.path.join(root, name)] = os.path.getsize(os.path.join(root, name))
            elif not ext:
                dict_of_sizes[os.path.join(root, name)] = os.path.getsize(os.path.join(root, name))

    dict_of_files = flipp_dict(dict_of_sizes)
    dict_to_print = check_num_of_val(dict_of_files)
    print_sorted(dict_of_files, sorting_option)


if __name__ == "__main__":
    main()

