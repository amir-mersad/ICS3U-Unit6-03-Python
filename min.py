#!/usr/bin/env python3

# Created by: Amir Mersad
# Created on: December 2019
# This program finds the min number

import random


def min_num(input_list):
    # Process
    current_min = input_list[0]
    for counter in input_list:
        if counter < current_min:
            current_min = counter
    return current_min


def main():
    # This function gets the input and passes it to another function
    number_list = []

    # Input and part of Process
    for counter in range(1, 10 + 1):
        number = random.randint(1, 100)
        number_list.append(number)
        print(number)

    # Passing to another function
    min_number = min_num(number_list)

    # Output
    print(f"\n{min_number}")


if __name__ == "__main__":
    main()
