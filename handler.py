import sys
import os


def main():
    args = sys.argv
    # os.chdir(root_folder)
    try:
        root_folder = args[1]
        for root, dirs, files in os.walk(root_folder):
            for name in files:
                print(os.path.join(root, name))
    except IndexError:
        print("Directory is not specified")




if __name__ == "__main__":
    main()