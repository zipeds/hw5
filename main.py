import sqlite3
db = sqlite3.connect('Students')
r = db.cursor()

r.execute('''CREATE TABLE IF NOT EXISTS
students(
name text, 
surname text,
hobby text, 
birth_year integer,
point integer           
)''')
r.execute("INSERT INTO students VALUES('Diablo', 'Tempest', 'swordsswords', 2005, 12)")
r.execute("INSERT INTO students VALUES('Rimuru', 'Tempest', 'swords', 2005, 9)")
r.execute("INSERT INTO students VALUES('Tooru', 'Tempest', 'swords', 2004,9)")
r.execute("INSERT INTO students VALUES('Hakurou', 'Sato', 'swords', 2006, 10)")
r.execute("INSERT INTO students VALUES('Key', 'Ito', 'swords', 2006, 8)")
r.execute("INSERT INTO students VALUES('Gobuta', 'Tanaka', 'swords', 2006, 7)")
r.execute("INSERT INTO students VALUES('Ranga', 'Tempest', 'swords', 2005, 9)")
r.execute("INSERT INTO students VALUES('Milim', 'Nava', 'swords', 2004, 10)")
r.execute("INSERT INTO students VALUES('Shuna', 'Yamadzakina', 'swords', 2006, 10)")
r.execute("INSERT INTO students VALUES('Shion', 'Maede', 'swords', 2005, 8)")
r.execute("SELECT * FROM students")

r.execute("UPDATE students SET name = 'genius' WHERE point >=10")
r.execute("SELECT rowid, * FROM students")

item = r.fetchall()
for i in item:
    print(i)
for i in item:
    surname = i[1]
    if len(surname) >= 10:
        print(surname)
    else:
        ...
r.execute("SELECT rowid, name FROM students WHERE name = 10 ")
r.execute("DELETE FROM students WHERE rowid % 2 = 0")

print(r.fetchall())
db.commit()
db.close()
