#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    sum = 0
    list = sys.argv[:]
    for item in list:
        try:
            sum = sum + int(item)
        except ValueError:
            sum = 0
    print("{}".format(sum))
