import matplotlib as plt
from sys import argv

def menu():
    print("1.) Parabolic: n^{2}")
    return 0

def calculateNums(arg):
    #code
    return 0


def main(args):

    choice = 0
    while True:
        menu()
        try:
            choice = int(input("Please choose which sequence to plot: "))
        except ValueError:
            print("Please enter a number! ")

        if choice == -1:
            break


if __name__ == '__main__':
    main(argv)
