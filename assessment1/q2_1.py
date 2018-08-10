#!/usr/bin/env python3

import sqlite3

connection = sqlite3.connect('q2_1.db',check_same_thread=False)
cursor = connection.cursor()

#few to many
cursor.execute(
	"""CREATE TABLE states(
		Id INTEGER PRIMARY KEY AUTOINCREMENT,
		StateName TEXT
	);"""
)

cursor.execute(
	"""CREATE TABLE cities(
		CityId INTEGER PRIMARY KEY AUTOINCREMENT,
		CityName TEXT,
		StateId INTEGER,
		FOREIGN KEY(StateId) REFERENCES states(Id)
	);"""
)

cursor.execute(
	"""CREATE TABLE parks(
		ParkId INTEGER PRIMARY KEY AUTOINCREMENT,
		CityName TEXT,
		StateId INTEGER,
		FOREIGN KEY(StateId) REFERENCES states(Id)
	);"""
)

cursor.close()
connection.close()

