# -*- coding: utf-8 -*-
# Created by MOSCA Marc on February 03 2021.

from hashlib import sha256
from system import System
from database import Database

class Commands:
    def __init__(self):
        self.system = System()
        self.database = Database()

    def helpCommand(self):
        print('\nVoici les commandes disponible : ')
        print('-' * 30)
        print('"?" vous permet de voir toutes les commandes disponibles.')
        print('"tchat" vous permet de vous rendre sur le tchat.')
        print('"mute" vous permet de bloquer la parole d\'un utilisateur.') 
        print('"unmute" vous permet de rendre la parole à un utilisateur.') 
        print('"mute-tchat" vous permet de rendre tout le tchat muet.')
        print('"unmute-tchat" vous permet de rendre le tchat de nouveau disponible.')
        print('"ban" vous permet de bannir un utilisateur.') 
        print('"unban" vous permet de dé-bannir un utilisateur.') 
        print('"delete-user" vous permet de supprimer un utilisateur.')
        print('"delete-message-user" vous permet de supprimer tous les messages d\'un utilisateur.')
        print('"delete-message" vous permet de supprimer un message dans le tchat.')
        print('"delete-server-message" vous permet de supprimer tout les messages d\'un serveur.')
        print('"add-server" vous permet d\'ajouter un serveur de tchat.') 
        print('"remove-server" vous permet de supprimer un serveur de tchat.')
        print('"add-admin" vous permet d\'ajouter le rôle administrateur à un utilisateur.')
        print('"remove-admin" vous permet de supprimer le rôle administrateur à un utilisateur.')
        print('"exit" vous permet de quitter le programme.')
        print('-' * 30)
        return input(': ')

    def muteCommand(self):
        user_email_to_mute = input('Quel est l\'adresse mail de l\'utilisateur que vous souhaitez rendre muet ? : ').lower()
        if self.database.verifyUserRegisterRequest(user_email_to_mute):
            if self.database.isAdminRequest(user_email_to_mute)[0] != 0: self.system.exitProgram('Vous ne pouvez pas rendre muet un utilisateur qui possède un role.')
            self.database.userToMuteRequest(user_email_to_mute) 

    def unmuteCommand(self):
        user_email_to_unmute = input('Quel est l\'adresse mail de l\'utilisateur a qui vous souhaitez rendre la parole ? : ').lower()
        if self.database.verifyUserRegisterRequest(user_email_to_unmute):
            if self.database.isMutedRequest(user_email_to_unmute) == None: self.system.exitProgram('Vous ne pouvez rendre la parole qu\'à un utilisateur qu\'i ne la plus.')
            self.database.userToUnmuteRequest(user_email_to_unmute)

    def muteTchatGlobalCommand(self):
        server_name_to_mute = input('Quel est le nom du serveur que vous souhaitez rendre muet ? : ')
        verify_server_exist = self.database.verifyServerExistRequest(server_name_to_mute)
        if verify_server_exist == [] or verify_server_exist == None: self.system.exitProgram('Le serveur demandé n\'est pas disponible.')
        if self.database.isMutedServerRequest(server_name_to_mute)[0] == 1: self.system.exitProgram('Le serveur est déjà muet.')
        self.database.muteTchatGlobalRequest(server_name_to_mute)

    def unmuteTchatGlobalCommand(self):
        server_name_to_mute = input('Quel est le nom du serveur que vous souhaitez rendre muet ? : ')
        verify_server_exist = self.database.verifyServerExistRequest(server_name_to_mute)
        if verify_server_exist == [] or verify_server_exist == None: self.system.exitProgram('Le serveur demandé n\'est pas disponible.')
        if self.database.isMutedServerRequest(server_name_to_mute)[0] == 0: self.system.exitProgram('Le serveur n\'est pas muet.')
        self.database.unmuteTchatGlobalRequest(server_name_to_mute)
    
    def banCommand(self):
        user_email_to_ban = input('Quel est l\'adresse mail de l\'utilisateur que vous souhaitez bannir ? : ').lower()
        if self.database.verifyUserRegisterRequest(user_email_to_ban):
            if self.database.isAdminRequest(user_email_to_ban)[0] != 0: self.system.exitProgram('Vous ne pouvez pas bannir un utilisateur qui possède un role.')
            self.database.userToBanRequest(user_email_to_ban)

    def unbanCommand(self):
        user_email_to_unban = input('Quel est l\'adresse mail de l\'utilisateur que vous souhaitez débannir ? : ').lower()
        if self.database.verifyUserRegisterRequest(user_email_to_unban):
            if self.database.isBannedRequest(user_email_to_unban) == None: self.system.exitProgram('Vous ne pouvez débannir un utilisateur qui n\'est pas banni.')
            self.database.userToUnbanRequest(user_email_to_unban)

    def deleteUserCommand(self):
        user_email_to_delete = input('Quel est l\'adresse mail de l\'utilisateur que vous souhaitez supprimer ? : ').lower()
        if self.database.verifyUserRegisterRequest(user_email_to_delete): self.database.deleteUserRequest(user_email_to_delete)

    def deleteMessageInTchatCommand(self):
        server_name = input('Quel est le nom du serveur auquel vous souhaitez supprimer un message ? : ')
        message = input('Quel est le message à supprimer ? : ')
        self.database.deleteMessageInTchatRequest(server_name, message)

    def deleteAllMessageUserCommand(self):
        user_email_to_message_delete = input('Quel est l\'adresse mail de l\'utilisateur auquel vous souhaitez supprimer les messages ? : ').lower()
        if self.database.verifyUserRegisterRequest(user_email_to_message_delete): self.database.deleteAllUserMessageRequest(user_email_to_message_delete)

    def deleteAllMessageServerCommand(self):
        server_name_to_delete_message = input('Quel est le nom du serveur auquel vous souhaitez supprimer tout les message ? : ')
        verify_server_exist = self.database.verifyServerExistRequest(server_name_to_delete_message)
        if verify_server_exist == [] or verify_server_exist == None: self.system.exitProgram('Le serveur demandé n\'est pas disponible.')
        self.database.deleteAllMessageServerRequest(server_name_to_delete_message)

    def addServeurCommand(self):
        server_name = input('Quel est le nom du serveur que vous souhaitez créer ? : ')
        server_password = input('Veuillez saisir un mot de passe pour le serveur : ')
        server_password_hashed = sha256(server_password.encode('utf-8')).hexdigest()
        verify_server_name = self.database.verifyServerExistRequest(server_name)
        if verify_server_name == None or verify_server_name == []: self.database.addServerRequest(server_name, server_password_hashed)
        else: self.system.exitProgram('Le nom du serveur n\'est pas disponible.')

    def removeServerCommand(self):
        server_name = input('Quel est le nom du serveur que vous souhaitez supprimer ? : ')
        verify_server_name = self.database.verifyServerExistRequest(server_name)
        if verify_server_name == None or verify_server_name == []: self.system.exitProgram('Le serveur n\'est pas disponible.')
        self.database.removeServerRequest(server_name)

    def addAdminCommand(self):
        user_email_to_add_admin = input('Quel est l\'adresse mail du compte auquel vous souhaitez mettre le rôle administrateur ? : ')
        if self.database.verifyUserRegisterRequest(user_email_to_add_admin): self.database.addAdminRequest(user_email_to_add_admin)

    def removeAdminCommand(self):
        user_email_to_remove_admin = input('Quel est l\'adresse mail du compte auquel vous souhaitez retiré le rôle administrateur ? : ')
        if self.database.verifyUserRegisterRequest(user_email_to_remove_admin): self.database.removeAdminRequest(user_email_to_remove_admin)
