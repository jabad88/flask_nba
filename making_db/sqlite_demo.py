import sqlite3

con = sqlite3.connect('players.db')
curr = con.cursor()

# CREATED TABLE BELOW
# curr.execute("""CREATE TABLE players (
#              id INTEGER PRIMARY KEY AUTOINCREMENT,
#              first test NOT NULL,
#              last text NOT NULL,
#              quote text NOT NULL
# )""")

# con.execute("INSERT INTO players ('first','last','quote') VALUES ('LeBron', 'James', 'You can''t be afraid to fail. It''s the only way you succeed - you''re not gonna succeed all the time, and I know that.')")

# con.execute("INSERT INTO players ('first','last','quote') VALUES ('Kobe', 'Bryant', 'Everything negative—pressure, challenges—is all an opportunity for me to rise.')")

curr.execute("SELECT * FROM players")

print(curr.fetchall())

con.commit()

con.close()