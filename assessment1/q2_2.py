#!/usr/bin/env python3

import sqlite3

connection = sqlite3.connect('q2_2.db',check_same_thread=False)
cursor = connection.cursor()

cursor.execute(
	"""CREATE TABLE doctors(
		docId INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT
	);"""
)

cursor.execute(
	"""CREATE TABLE patients(
		patId INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT
	);"""
)

cursor.execute(
	"""CREATE TABLE doctors_patients(
		pk INTEGER PRIMARY KEY AUTOINCREMENT,
		doctorId INTEGER,
		patientId INTEGER,
		FOREIGN KEY(doctorId) REFERENCES doctors(docId),
		FOREIGN KEY(patientId) REFERENCES patients(patId)	
	);"""
)

cursor.close()
connection.close()

