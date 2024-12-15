import sqlite3

con = sqlite3.connect('not_telegram.db')
cursor = con.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
ID INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email  TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')
# cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')
# for a in range(1, 11):
#
#     cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES(?, ?, ?, ?)',
#                    (f"user{a}", f"example{a}@gmail.com", f"{a}0", "1000"))
#
# for x in range(1, 11, 2):
#     cursor.execute('UPDATE Users set balance = ? WHERE username = ?', (500, f"user{x}"))
#
# for x in range(1, 11, 3):
#     cursor.execute('DELETE FROM Users WHERE username=?', (f"user{x}",))
#
# cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != ?', (60,))
# users = cursor.fetchall()
#
# for user in users:
#     print(f"Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс {user[3]}")

# cursor.execute('DELETE FROM Users WHERE id = ?', (6,))

cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]
cursor.execute('SELECT SUM(balance) FROM Users')
all_balances = cursor.fetchone()[0]
print(all_balances / total_users)


con.commit()
con.close()
