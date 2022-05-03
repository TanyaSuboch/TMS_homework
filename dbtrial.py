import sqlite3

db = sqlite3.connect('trialdatabase.db')
sql = db.cursor()

#one-to-one
sql.execute("CREATE TABLE clients(
    id INTEGER PRIMARY KEY,
    client_name TEXT NOT NULL,
    client_surname TEXT NOT NULL
    )
    ")

sql.execute("CREATE TABLE accounts(
    id INTEGER PRIMARY KEY,
    login TEXT NOT NULL,
    password TEXT NOT NULL,
    client_id INTEGER UNIQUE NOT NULL,
    FOREIGN KEY (client_id) REFERENCES clients(id)
    )
    ")

db.commit()

#one-to-many
sql.execute("CREATE TABLE clients(
    id INTEGER PRIMARY KEY,
    client_name TEXT NOT NULL,
    client_surname TEXT NOT NULL
    )
    ")
    
sql.execute("CREATE TABLE phone_numbers(
    phone_number_id INTEGER PRIMARY KEY,
    phone_number TEXT NOT NULL,
    telephone_company TEXT NOT NULL,
    client_id INTEGER NOT NULL,
    FOREIGN KEY (client_id) REFERENCES clients(id)
    )
    ")

