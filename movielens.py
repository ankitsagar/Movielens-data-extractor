import sqlite3

conn = sqlite3.connect('movielens.sqlite')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS Movies (m_id INTEGER, m_name TEXT UNIQUE, category_id INTEGER) """)
cur.execute('''CREATE TABLE IF NOT EXISTS Tags(m_id INTEGER, usr_id INTEGER, tag_id INTEGER )''')
cur.execute('''CREATE TABLE IF NOT EXISTS Ratings(usr_id INTEGER, m_id INTEGER, ratings INTEGER)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Tag(id INTEGER PRIMARY KEY, tag TEXT UNIQUE)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Category (id INTEGER PRIMARY KEY, category TEXT UNIQUE)''')

movie_file = open('movies.dat')
for line in movie_file:
    line = line.strip()
    line = line.split('::')
    m_id = line[0]
    movie = line[1]
    genre = line[2]
    cur.execute('''INSERT OR IGNORE INTO Category (category) VALUES (?)''', (genre, ))
    cur.execute('SELECT id FROM Category WHERE category = ?', (genre,))
    genre_id = cur.fetchone()[0]
    cur.execute('''INSERT OR IGNORE INTO Movies (m_id, m_name, category_id) VALUES (?, ?, ?)''',(m_id, movie, genre_id))
conn.commit()
print("inserted movies")
rating_file = open('ratings.dat')
for line in rating_file:
    line = line.strip()
    line = line.split("::")
    usr_id = line[0]
    m_id = line[1]
    rating = line[2]
    cur.execute('''INSERT OR IGNORE INTO Ratings (usr_id, m_id, ratings) VALUES (?, ?, ?)''',(usr_id, m_id, rating))
conn.commit()
print("inserted RAtings ")
tags_file = open('tags.dat')
for line in tags_file:
    line = line.strip()
    line = line.split('::')
    usr_id = line[0]
    m_id = line[1]
    tags = line[2]
    cur.execute('''INSERT OR IGNORE INTO Tag (tag) VALUES (?)''', (tags, ))
    cur.execute('SELECT id FROM Tag WHERE tag = ?', (tags, ))
    row = cur.fetchone()
    tag_id = row[0]
    cur.execute('INSERT OR IGNORE INTO Tags (m_id, usr_id, tag_id) VALUES (?, ?, ?)', (m_id, usr_id, tag_id))
conn.commit()
print("inserted all files")