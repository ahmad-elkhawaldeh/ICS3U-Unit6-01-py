#!/usr/bin/env python3

# Created by: Ahmad
# Created on: Jan 2021
# This program uses an array

import random


def main():
    # this function uses an array

    list1 = []
    for loop in range(1, 11):
        # generating random numbers
        number = random.randint(1, 100)
        print("The random number is:", number)

        list1.append(number)

    print("\nThe average is", sum(list1)/10)


if __name__ == "__main__":
    main()
