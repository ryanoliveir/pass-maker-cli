# -*- coding: utf-8 -*-

from passmaker import Passmaker


def readline(msg):
    while True:    
        try:
            return int(input(msg))
        except (TypeError, ValueError):
            print("[!] Must be an integer...\n")

unicode = '\u20E0'
numChar = readline(f"pmaker {unicode}  Number of characters:\n$ ")

numPass = readline(f"pmaker {unicode}  Number of passwords\n$ ")





pmaker = Passmaker(numChar, numPass, "all")
pmaker.set_passConfig()



print(*pmaker.construct(), sep="\n")