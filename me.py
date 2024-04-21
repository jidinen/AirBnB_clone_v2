#!/bin/python3 

def hello_world(start, end):
    """ A program that prints even number"""
    for i in range(start, end + 1):
        if i % 2 == 0:
            print("{} is an even number.".format(i))


start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

hello_world(start, end)
