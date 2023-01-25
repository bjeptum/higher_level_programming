#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if i < 98:
            print("{num:02d}".format(num=i*10+j), end=", ")
        else:
            print("{}".format(i*10+j))
