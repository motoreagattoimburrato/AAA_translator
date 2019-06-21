#!/usr/bin/env python3
import sys

def AAATRANSLATOR(aaa):
    for aa in aaa:
        for a in range(len(aa)):
            print("A", end=""),
        print("")

# Debug
#print(sys.argv);
sys.argv.remove(sys.argv[0])

AAATRANSLATOR(sys.argv)
