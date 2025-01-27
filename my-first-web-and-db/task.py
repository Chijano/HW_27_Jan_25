import sqlite3
from task_data import *
from task_create import *

conn = sqlite3.connect("chat_app.db")

cur = conn.cursor()

cur.execute(users_create_table)
cur.execute(rooms_create_table)
cur.execute(messages_create_table)
#cur.execute(insert_users)
#cur.execute(insert_rooms)
#cur.execute(insert_messages)
conn.commit()

# Task 1: Nájsť používateľov, ktorí poslali správy do konkrétnej miestnosti (napr. room1).
cur.execute("""
SELECT DISTINCT UserName, r.Name
FROM messages m
INNER JOIN users u
ON m.User_id = u.id
INNER JOIN rooms r
ON m.room_id = r.id
WHERE room_id = 1
""")
data1 = cur.fetchall()
print(data1)

# Task 2: Počítať, koľko rôznych používateľov poslalo správy do jednotlivých miestností
cur.execute("""
SELECT COUNT(DISTINCT(username)), r.name
FROM messages m
INNER JOIN users u
ON m.User_id = u.id
INNER JOIN rooms r
ON m.room_id = r.id
GROUP BY room_id
""")
data2 = cur.fetchall()
print(data2)

# Task 3: Nájsť miestnosti, do ktorých konkrétny používateľ (napr. user2) poslal správy.
cur.execute("""
SELECT DISTINCT R.name
FROM messages m
INNER JOIN users u
ON m.User_id = u.id
INNER JOIN rooms r
ON m.room_id = r.id
WHERE Username = 'user2'
""")
data3 = cur.fetchall()
print(data3)

# Task 4: Zobraziť počet správ, ktoré poslal každý používateľ.
cur.execute("""
SELECT COUNT(message), UserName
FROM messages m
INNER JOIN users u
ON m.User_id = u.id
INNER JOIN rooms r
ON m.room_id = r.id
GROUP BY UserName
""")
data4 = cur.fetchall()
print(data4)

# Task 5 Zobraziť zoznam miestností spolu s počtom správ, ktoré poslali jednotliví používatelia.
cur.execute("""
SELECT r.name, username, COUNT(message)
FROM messages m
INNER JOIN users u
ON m.User_id = u.id
INNER JOIN rooms r
ON m.room_id = r.id
GROUP BY r.name, u.username
order by r.id, u.id asc
""")
data5 = cur.fetchall()
print(data5)


print("DONE")
