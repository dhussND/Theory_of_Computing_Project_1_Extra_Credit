#!/usr/bin/env python3

'''
Extra credit file: converts test_cases.txt to .cnf
'''

import sys

def main():
    i = 1

    while True:
        line1 = sys.stdin.readline()
        line2 = sys.stdin.readline()

        if not line1 or not line2:
            break

        line1 = line1.split(":")
        line2 = line2.split(":")

        if line1[1][1] == 'H':
            print(f"c, {i}, h")
        else:
            print(f"c, {i}, n")
        
        line1[2] = eval(line1[2].strip())
        line2[2] = eval(line2[2].strip())

        print(f"p, u, {len(line1[2])}, {len(line2[2])}")

        
        nodes = ", ".join(str(node) for node in line1[2])
        print(f"v, {nodes}")

        
        for edge in line2[2]:
            print(f"e, {edge[0]}, {edge[1]}")



if __name__ == "__main__":
    main()