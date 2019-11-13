#!/usr/bin/env python3

# Created by: RJ Fromm
# Created on: Nov 2019
# This program finds the largest and smallest numbers entered


def main():

    my_list = []

    try:
        number = int(input('How many numbers: '))
        for n in range(number):
            numbers = int(input('Enter number '))
            my_list.append(numbers)
        print("Largest number in the list is :", max(my_list),
              "\nSmallest number in the list is :", min(my_list))
    except Exception:
        print("That is not a number")


if __name__ == "__main__":
    main()
