import sqlite3

conn = sqlite3.connect('18-dars.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS city (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city TEXT NOT NULL,
        country TEXT NOT NULL,
        postcode INTEGER NOT NULL
    )
''')
conn.commit()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS book (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(50) NOT NULL,
        author VARCHAR(50) NOT NULL,
        category TEXT NOT NULL,
        price REAL
    )
''')
conn.commit()

cursor.execute('''
    INSERT INTO city (city, country, postcode)
    VALUES 
        ("city1", "country1", 1),
        ("city2", "country2", 2),
        ("city3", "country3", 3),
        ("city4", "country4", 4),
        ("city5", "country5", 5),
        ("city6", "country6", 6),
        ("city7", "country7", 7),
        ("city8", "country8", 8),
        ("city9", "country9", 9),
        ("city10", "country10", 10)
''')
conn.commit()

cursor.execute("SELECT * FROM city WHERE country = 'country1'")
country1 = cursor.fetchall()
print(country1)


cursor.execute('''
    INSERT INTO book (name, author, category)
    VALUES 
        ("book1", "author1", "category1"),
        ("book2", "author2", "category2"),
        ("book3", "author3", "category3"),
        ("book4", "author4", "category4"),
        ("book5", "author5", "category5"),
        ("book6", "author6", "category6"),
        ("book7", "author7", "category7"),
        ("book8", "author8", "category8"),
        ("book9", "author9", "category9"),
        ("book10", "author10", "category10")
''')
conn.commit()

cursor.execute("SELECT * FROM book WHERE author = 'author1'")
author1 = cursor.fetchall()
print(author1)


cursor.execute('''
    CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50),
        age INTEGER
    )
''')
conn.commit()

cursor.execute('''
    INSERT INTO user (first_name, age, last_name)
    VALUES
        ("ali", 25, null),
        ("vali", 25, "valiey"),
        ("alibek", 26, "alibekov")
''')
conn.commit()

cursor.execute("SELECT * FROM user WHERE age = 25")
users = cursor.fetchall()
print(users)

cursor.execute("SELECT first_name, last_name FROM user WHERE age = 25")
users = cursor.fetchall()
print(users)

cursor.execute("SELECT first_name, last_name FROM user WHERE id = 3")
users = cursor.fetchall()
print(users)

conn.close()