# -*- coding: utf-8 -*-
# Created by MOSCA Marc on February 03 2021.

import datetime
from hashlib import sha256
from database import Database
from system import System

class Tchat:
    def __init__(self):
        self.database = Database()
        self.system = System()

    def menu(self, username, user_email, server_name):
        self.system.clearTerminal()
        print(('-'*9) + f' Tchat {server_name} '+ ('-' *9))
        print(f'Bienvenue {username} sur le chat du serveur {server_name}.\n')
        self.database.retrieveMessageRequest(server_name)
        while self.message(username, user_email, server_name):
            self.menu(username, user_email, server_name)

    def message(self, username, user_email, server_name):
        message = input(': ')
        print('')
        result = self.database.isMutedRequest(user_email)
        server_mute = self.database.isMutedServerRequest(server_name)
        if server_mute[0] == 1: self.system.exitProgram('Vous ne pouvez pas envoyer de message car le serveur à été réduit au silence.')
        if message == 'exit': self.system.exitProgram('Vous quittez le programme.')
        if result != None and result[0] != 0: self.system.exitProgram('Vous ne pouvez pas envoyer de message car vous avez été réduit au silence.')
        self.database.insertMessageTchatRequest(user_email, username, datetime.datetime.now().strftime("%d/%m/%Y - %H:%M"), message.capitalize(), server_name)
        return True

    def server(self, username, user_email):
        self.system.clearTerminal()
        print(('-'*9) + ' Choix du serveur '+ ('-' *9))
        print('Veuillez entrer le nom du serveur que vous souhaitez rejoindre.\n')
        self.database.retrieveServeurRequest()
        server_name = input(': ')
        verify_server_exist = self.database.verifyServerExistRequest(server_name)
        if verify_server_exist == [] or verify_server_exist == None: self.system.exitProgram('Le serveur demandé n\'est pas disponible.')
        user_server_password = input('Veuillez saisir le mot de passe du serveur : ')
        user_server_password_hashed = sha256(user_server_password.encode('utf-8')).hexdigest()
        if user_server_password_hashed != verify_server_exist[2]: self.system.exitProgram('Mauvais mot de passe.')
        self.menu(username, user_email, server_name)
