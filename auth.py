# -*- coding: utf-8 -*-
# Created by MOSCA Marc on February 03 2021.

from hashlib import sha256
from database import Database
from system import System
from tchat import Tchat
from admin import Admin

class Authentification:
    def __init__(self):
        self.database = Database()
        self.system = System()
        self.tchat = Tchat()
        self.admin = Admin()

    def menu(self):
        self.system.clearTerminal()
        print(('-'*9) + ' Connexion '+ ('-' *9))
        print('1. Se connecter')
        print('2. S\'inscrire')
        print('Q. Quitter')
        print('-'*29)
        choice = str(input(': ')).lower()
        while choice != 'q' and choice != '1' and choice != '2':
            print('Désolé, je ne comprend pas !')
            self.menu()
        if choice == '1': self.connection()
        elif choice == '2': self.register()
        else: self.system.exitProgram('Vous quittez le programme.')

    def register(self):
        register_username = input('Veuillez saisir votre nom d\'utilisateur : ').capitalize()
        register_user_email = input('Veuillez saisir votre adresse mail : ').lower()
        register_user_password = input('Veuillez saisir un mot de passe : ')
        register_user_password_hashed = sha256(register_user_password.encode('utf-8')).hexdigest()
        database_user_informations = self.database.researchUserRequest(register_user_email)
        if database_user_informations != []: self.system.exitProgram('L\'adresse mail est déjà utiliser !')
        self.database.insertUserRequest(register_username, register_user_email, register_user_password_hashed)

    def connection(self):
        connection_user_email = input('Veuillez saisir votre adresse mail : ').lower()
        connection_user_password = input('Veuillez saisir un mot de passe : ')
        connection_user_password_hashed = sha256(connection_user_password.encode('utf-8')).hexdigest()
        database_user_informations = self.database.researchUserRequest(connection_user_email)
        if database_user_informations == []: self.system.exitProgram('L\'adresse mail est incorrecte ou n\'exite pas.')
        if connection_user_password_hashed != database_user_informations[0][3]: self.system.exitProgram('Mauvais mot de passe.')
        if self.database.isBannedRequest(connection_user_email)[0] == 0:
            if self.database.isAdminRequest(connection_user_email)[0] == 0: self.tchat.server(database_user_informations[0][1], connection_user_email)
            else: self.admin.menu(database_user_informations[0][1], connection_user_email)
        else: self.system.exitProgram('Vous ne pouvez pas rejoindre car vous avez été banni.')

    def cryptage(self):
        return 0
