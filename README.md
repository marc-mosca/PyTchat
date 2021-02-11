# PyTchat
 A chat program with servers, a login system and administrative controls.

### Contents: 
- Description of the project
- Used languages
- Required
- Database description

### Description of the project

The program is a chat with servers. When the programme is launched, one can log in or register, when a user who does not have the admin role logs in, he will be redirected to the selection of chat servers. If the user logging in has the admin role then he will be redirected to a command space where he can enter and use commands to administer the servers, users and chat.
Small note, for the first connection, you have to manually set the admin role to your account to be able to access the moderation control panel.

### Used languages ?

+ Python

### Required

+ A database file named 'database.sqlite3'.

### Database description

+ CREATE TABLE "users" ("id"	INTEGER NOT NULL UNIQUE, "username"	TEXT, "email"	TEXT NOT NULL, "password"	TEXT, "admin"	INTEGER NOT NULL, "mute"	INTEGER NOT NULL, "ban"	INTEGER NOT NULL, PRIMARY KEY("id" AUTOINCREMENT));
+ CREATE TABLE "tchat_server" ("id"	INTEGER NOT NULL UNIQUE, "name"	TEXT UNIQUE, "password"	TEXT, "mute"	INTEGER NOT NULL, PRIMARY KEY("id" AUTOINCREMENT));
+ CREATE TABLE "tchat_message" ("id"	INTEGER NOT NULL UNIQUE,	"email"	TEXT,	"username"	TEXT,	"date"	NUMERIC,	"message"	TEXT,	"server_name"	TEXT,	PRIMARY KEY("id" AUTOINCREMENT));

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
