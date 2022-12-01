#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    length = (len(sys.argv)-1)

    if length == 0:
        print("{} arguments.".format(length))
    elif length == 1:
        print("{} argument:".format(length))
    else:
        print("{} arguments:".format(length))
    count = 1
    list = sys.argv[1:]
    for item in list:
        print("{}: {}".format(count, item))
        count = count + 1
