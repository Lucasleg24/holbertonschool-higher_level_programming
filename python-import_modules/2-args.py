#!/usr/bin/python3
import sys

if __name__ == "__main__":

    print(f"{len(sys.argv) - 1} arguments:")
    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"{i}: {arg}")
