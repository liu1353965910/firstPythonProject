# -*- coding: UTF-8 -*-

with open("pi_digits.txt", "a") as fi:
    fi.write("3256")


with open("pi_digits.txt") as file_object:
    content = file_object.read()
    print(content.rstrip())

with open("pi_digits.txt") as file_object:
    for line in file_object:
        print(line.rstrip())




