# -*- coding: utf-8 -*-
# Created by MOSCA Marc on February 03 2021.

from tchat import Tchat
from system import System
from commands import Commands

class Admin:
    def __init__(self):
        self.tchat = Tchat()
        self.system = System()
        self.command = Commands()

    def menu(self, username, user_email):
        self.system.clearTerminal()
        print('Bienvenue dans la console de modération du tchat.')
        print('Si vous souhaitez savoir les commandes disponibles taper : "?".')
        choice = input(': ')

        while choice != '?' and choice != 'tchat' and choice != 'mute' and choice != 'unmute' and choice != 'mute-tchat' and choice != 'unmute-tchat' and choice != 'ban' and choice != 'unban' and choice != 'delete-user' and choice != 'delete-message-user' and choice != 'delete-message' and choice != 'delete-server-message' and choice != 'add-server' and choice != 'remove-server' and choice != 'add-admin' and choice != 'remove-admin' and choice != 'exit':
            self.menu(username, user_email)

        while choice == '?': choice = self.command.helpCommand()
        if choice == 'tchat': self.tchat.server(username, user_email)
        elif choice == 'mute': self.command.muteCommand()
        elif choice == 'unmute': self.command.unmuteCommand()
        elif choice == 'mute-tchat': self.command.muteTchatGlobalCommand()
        elif choice == 'unmute-tchat': self.command.unmuteTchatGlobalCommand()
        elif choice == 'ban': self.command.banCommand()
        elif choice == 'unban': self.command.unbanCommand()
        elif choice == 'delete-user': self.command.deleteUserCommand()
        elif choice == 'delete-message-user': self.command.deleteAllMessageUserCommand()
        elif choice == 'delete-message': self.command.deleteMessageInTchatCommand()
        elif choice == 'delete-server-message': self.command.deleteAllMessageServerCommand()
        elif choice == 'add-server': self.command.addServeurCommand()
        elif choice == 'remove-server': self.command.removeServerCommand()
        elif choice == 'add-admin': self.command.addAdminCommand()
        elif choice == 'remove-admin': self.command.removeAdminCommand()
        else: self.system.exitProgram('Vous quittez le programme.')
