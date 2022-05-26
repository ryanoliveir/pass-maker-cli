# -*- coding: utf-8 -*-

from art import *
from progress.bar import ChargingBar
from time import sleep
import random
import string
import platform
import sys




#QUIT_FUNCTION
def conti_():
    option = input("\nDo you want to continue? [y/n] ")
    if option == 'y' or option == 'Y':
        pass
    else:
        sys.exit(0)


#LOAD_BAR_FUNCTION
def set_load_bar(type_os, pass_number):
    if type_os == True:
        #OS: Linux

        bar =  ChargingBar('Processing... ', max = pass_number)
        for _ in range(0, pass_number):
            sleep(.1)
            bar.next()
        bar.finish() 
    elif type_os == False:
        #OS: Windows
        print('Loading...')
        for a in range(0,50):
            print("|" if a == 0 else "", end="" ,flush=True)
            print(u"\u2588", end='', flush=True)
            sleep(.05)
        print("| 100.0% Done!")


#SET_COLORS_FUNCTIONS
def set_color():

    RED_LINUX = '\033[1;31m'
    BLUE_LINUX = '\033[1;34m'
    GREEN_LINUX = '\033[1;32m'
    NONE_LINUX = '\033[m'

    def os_detection():
        os = platform.platform()
        if 'Windows' in os:
            return 'Windows'
        elif 'Linux' in os:
            return 'Linux'

    os = os_detection()
    
    if os == 'Windows':
        print('[*]Colors status: FALSE')
        colors_setting = [ '', '', '', '' ]
        return colors_setting, colors_setting[3] , False
    elif os == 'Linux':
        print('[*]Colors status: TRUE')
        colors_setting = [ RED_LINUX, BLUE_LINUX, GREEN_LINUX, NONE_LINUX ]
        return colors_setting , colors_setting[3], True


#PASSWORD_MAKER
def pass_maker(caracteres, password_number):
    data_base = string.ascii_uppercase + string.ascii_lowercase + string.digits + "!#$%&"
    list_pass = []

    for _ in range(0,password_number):
        list_caracteres = [] 
        for i in range(0,caracteres):
            list_caracteres.append(random.choice(data_base))
        password = "".join(list_caracteres)
        list_pass.append(password)
    
    #LOAD_BAR
    set_load_bar(bar_type, password_number) 
    
    #OUTPUT_PASSWORDS
    print('------------------------------------------------------------------------------\n'+ 'Passwords:\n')
    for i in list_pass:
        sleep(.1)
        print(f'{colors[2]}[+] {i} {none}')
    conti_()    


#SET_COLORS
colors, none, bar_type = set_color()

#TITLE
print(f'{colors[0]}')
print('------------------------------------------------------------------------------')
print('------------------------------------------------------------------------------')

title = text2art("PMaker",font='poison')
title = text2art("PMaker",font='poison')
print(title)

print("By: Ryan Oliveira")
print('------------------------------------------------------------------------------')
print('------------------------------------------------------------------------------')
print(f'{none}')
#END_TITLE


#LOOP_BEGIN
while True:
    
    print(f"{colors[1]}pmaker > {none}", end ="")
    print("Number of caracters:")
    c = int(input("=> "))

    print(f"{colors[1]}pmaker > {none}", end ="")
    print("Number of passwords: ")
    p = int(input("=> "))
    print('\n')
    pass_maker(c,p)

