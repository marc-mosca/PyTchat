# -*- coding: utf-8 -*-
# Created by MOSCA Marc on February 03 2021.

import sqlite3, os
from system import System

class Database:
    def __init__(self):
        self.system = System()
        self.cursor = None

    def connection(self):
        file_path = os.path.abspath(os.getcwd()+'/database.sqlite3')
        try: 
            connection = sqlite3.connect(file_path)
            self.cursor = connection.cursor()
            return connection
        except (Exception, sqlite3.Error) as error: print(error)

    def addServerRequest(self, server_name, password):
        try:
            if self.verifyServerExistRequest(server_name): return self.system.exitProgram('Le nom du serveur est déjà pris.')
            connection = self.connection()
            self.cursor.execute("INSERT INTO tchat_server (name, password, mute) VALUES (?, ?, ?)", (server_name, password, 0))
            connection.commit()
            return self.system.exitProgram(f'Le serveur {server_name} à bien été crée.')
        except (Exception, sqlite3.Error) as error: print(error)

    def addAdminRequest(self, user_email):
        try:
            connection = self.connection()
            self.cursor.execute("UPDATE users SET admin = (?) WHERE email = (?)", (1, user_email))
            connection.commit()
            return self.system.exitProgram(f'L\'utilisateur "{user_email}" à bien le rôle administrateur.')
        except (Exception, sqlite3.Error) as error: print(error)

    def insertUserRequest(self, username, user_email, user_password):
        try:
            connection = self.connection()
            self.cursor.execute("INSERT INTO users (username, email, password, admin, mute, ban) VALUES (?, ?, ?, ?, ?, ?)", (username, user_email, user_password, 0, 0, 0))
            connection.commit()
            return self.system.exitProgram('Votre inscription s\'est bien terminée !')
        except (Exception, sqlite3.Error) as error: print(error)

    def insertMessageTchatRequest(self, user_email, username, date, user_message, server_name):
        try:
            connection = self.connection()
            self.cursor.execute("INSERT INTO tchat_message (email, username, date, message, server_name) VALUES (?, ?, ?, ?, ?)", (user_email, username, date, user_message, server_name))
            connection.commit()
        except (Exception, sqlite3.Error) as error: print(error)

    def researchUserRequest(self, user_email):
        try:
            connection = self.connection()
            self.cursor.execute("SELECT * FROM users WHERE email = (?)", [user_email])
            connection.commit()
            return self.cursor.fetchall()
        except (Exception, sqlite3.Error) as error: print(error)

    def retrieveMessageRequest(self, server_name):
        try:
            connection = self.connection()
            self.cursor.execute("SELECT * FROM tchat_message WHERE server_name = (?)", [server_name])
            connection.commit()
            result = self.cursor.fetchall()
            for row in result: 
                print(f"{row[2]} : {row[4]}")
            print('\n' + '-'*30)
        except (Exception, sqlite3.Error) as error: print(error)

    def retrieveServeurRequest(self):
        try:
            connection = self.connection()
            self.cursor.execute("SELECT * FROM tchat_server")
            connection.commit()
            result = self.cursor.fetchall()
            for row in result: 
                print(f"Serveur : {row[1]}")
            print('\n' + '-'*30)
        except (Exception, sqlite3.Error) as error: print(error)

    def userToMuteRequest(self, user_email, mute_time = 0):
        try:
            connection = self.connection()
            self.cursor.execute("UPDATE users SET mute = (?) WHERE email = (?)", (1, user_email))
            connection.commit()
            return self.system.exitProgram(f'{user_email} à bien été rendu muet.')
        except (Exception, sqlite3.Error) as error: print(error)

    def userToUnmuteRequest(self, user_email):
        try:
            connection = self.connection()
            self.cursor.execute("UPDATE users SET mute = (?) WHERE email = (?)", (0, user_email))
            connection.commit()
            return self.system.exitProgram(f'{user_email} à bien retrouver la parole.')
        except (Exception, sqlite3.Error) as error: print(error)

    def userToBanRequest(self, user_email, ban_time = 0):
        try:
            connection = self.connection()
            self.cursor.execute("UPDATE users SET ban = (?) WHERE email = (?)", (1, user_email))
            connection.commit()
            return self.system.exitProgram(f'{user_email} à bien été banni.')
        except (Exception, sqlite3.Error) as error: print(error)
    
    def userToUnbanRequest(self, user_email):
        try:
            connection = self.connection()
            self.cursor.execute("UPDATE users SET ban = (?) WHERE email = (?)", (0, user_email))
            connection.commit()
            return self.system.exitProgram(f'{user_email} à bien été débanni.')
        except (Exception, sqlite3.Error) as error: print(error)

    def muteTchatGlobalRequest(self, server_name):
        try:
            connection = self.connection()
            self.cursor.execute("UPDATE tchat_server SET mute = (?) WHERE name = (?)", (1, server_name))
            connection.commit()
            return self.system.exitProgram(f'Le serveur "{server_name}" à bien été rendu muet.')
        except (Exception, sqlite3.Error) as error: print(error)

    def unmuteTchatGlobalRequest(self, server_name):
        try:
            connection = self.connection()
            self.cursor.execute("UPDATE tchat_server SET mute = (?) WHERE name = (?)", (0, server_name))
            connection.commit()
            return self.system.exitProgram(f'Le serveur "{server_name}"" à bien retrouver la parole.')
        except (Exception, sqlite3.Error) as error: print(error)

    def deleteUserRequest(self, user_email):
        try:
            connection = self.connection()
            self.cursor.execute("DELETE FROM users WHERE email = (?)", [user_email])
            connection.commit()
            return self.system.exitProgram(f'{user_email} à bien été supprimer.')
        except (Exception, sqlite3.Error) as error: print(error)

    def deleteAllUserMessageRequest(self, user_email):
        try:
            if not self.verifyUserGetMessageRequest(user_email): self.system.exitProgram('L\'utilisateur n\'a pas de message')
            connection = self.connection()
            self.cursor.execute("DELETE FROM tchat_message WHERE email = (?)", [user_email])
            connection.commit()
            return self.system.exitProgram(f'Les messages de {user_email} ont bien été supprimé.')
        except (Exception, sqlite3.Error) as error: print(error)

    def deleteMessageInTchatRequest(self, server_name, message):
        try:
            connection = self.connection()
            self.cursor.execute("DELETE FROM tchat_message WHERE (server_name = (?) and message = (?))", (server_name, message))
            connection.commit()
            return self.system.exitProgram('Le message à bien été supprimer.')
        except (Exception, sqlite3.Error) as error: print(error)

    def deleteAllMessageServerRequest(self, server_name):
        try:
            connection = self.connection()
            self.cursor.execute("DELETE FROM tchat_message WHERE server_name = (?)", [server_name])
            connection.commit()
            return self.system.exitProgram(f'Les messages de {server_name} ont bien été supprimé.')
        except (Exception, sqlite3.Error) as error: print(error)

    def removeServerRequest(self, server_name):
        try:
            connection = self.connection()
            self.cursor.execute("DELETE FROM tchat_server WHERE name = (?)", [server_name])
            connection.commit()
            return self.system.exitProgram(f'Le serveur "{server_name}"" a bien été supprimé.')
        except (Exception, sqlite3.Error) as error: print(error)

    def removeAdminRequest(self, user_email):
        try:
            connection = self.connection()
            self.cursor.execute("UPDATE users SET admin = (?) WHERE email = (?)", (0, user_email))
            connection.commit()
            return self.system.exitProgram(f'L\'utilisateur "{user_email}" ne possède plus le rôle administrateur.')
        except (Exception, sqlite3.Error) as error: print(error)

    def verifyUserRegisterRequest(self, user_email):
        try:
            connection = self.connection()
            self.cursor.execute("SELECT email FROM users WHERE email = (?)", [user_email])
            connection.commit()
            result = self.cursor.fetchone()
            if result == [] or result == None: self.system.exitProgram('L\'adresse mail n\'est pas enregistrer.')
            return True
        except (Exception, sqlite3.Error) as error: print(error)

    def verifyUserGetMessageRequest(self, user_email):
        try:
            connection = self.connection()
            self.cursor.execute("SELECT message FROM tchat_message WHERE email = (?)", [user_email])
            connection.commit()
            result = self.cursor.fetchall()
            if result == [] or result == None: return False
            return True
        except (Exception, sqlite3.Error) as error: print(error)

    def verifyServerExistRequest(self, server_name):
        try:
            connection = self.connection()
            self.cursor.execute("SELECT * FROM tchat_server WHERE name = (?)", [server_name])
            connection.commit()
            return self.cursor.fetchone()
        except (Exception, sqlite3.Error) as error: print(error)

    def isMutedRequest(self, user_email):
        try:
            connection = self.connection()
            self.cursor.execute("SELECT mute FROM users WHERE email = (?)", [user_email])
            connection.commit()
            return self.cursor.fetchone()
        except (Exception, sqlite3.Error) as error: print(error)

    def isMutedServerRequest(self, server_name):
        try:
            connection = self.connection()
            self.cursor.execute("SELECT mute FROM tchat_server WHERE name = (?)", [server_name])
            connection.commit()
            return self.cursor.fetchone()
        except (Exception, sqlite3.Error) as error: print(error)

    def isBannedRequest(self, user_email):
        try:
            connection = self.connection()
            self.cursor.execute("SELECT ban FROM users WHERE email = (?)", [user_email])
            connection.commit()
            return self.cursor.fetchone()
        except (Exception, sqlite3.Error) as error: print(error)

    def isAdminRequest(self, user_email):
        try:
            connection = self.connection()
            self.cursor.execute("SELECT admin FROM users WHERE email = (?)", [user_email])
            connection.commit()
            return self.cursor.fetchone()
        except (Exception, sqlite3.Error) as error: print(error)
