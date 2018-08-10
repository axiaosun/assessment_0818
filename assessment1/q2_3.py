#!/usr/bin/env python3

import sqlite3

connection = sqlite3.connect('q2_3.db',check_same_thread=False)
cursor = connection.cursor()

cursor.execute(
	"""CREATE TABLE users(
		uId INTEGER PRIMARY KEY AUTOINCREMENT,
		name VARCHAR,
		username VARCHAR,
		password VARCHAR,
		email VARCHAR
	);"""
)

cursor.execute(
	"""CREATE TABLE admins(
		aId INTEGER PRIMARY KEY AUTOINCREMENT,
		name VARCHAR,
		username VARCHAR,
		password VARCHAR,
		email VARCHAR
	);"""
)

cursor.execute(
	"""CREATE TABLE phone_numbers(
		pk INTEGER PRIMARY KEY AUTOINCREMENT,
		phone_number VARCHAR,
		userId INTEGER,
		adminId INTEGER,
		FOREIGN KEY(userId) REFERENCES users(uId),
		FOREIGN KEY(adminId) REFERENCES admins(aId)
	);"""
)

cursor.close()
connection.close()

