# -*- coding: utf-8 -*-
# Created by MOSCA Marc on February 03 2021.

import os, platform, sys

class System:
    def clearTerminal(self):
        if platform.system().lower() == 'linux' or platform.system().lower() == 'darwin': os.system("clear")
        else: os.system("cls")

    def exitProgram(self, message):
        print('\n' + str(message))
        exit()
