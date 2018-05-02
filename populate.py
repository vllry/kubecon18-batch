import database


conn = database.connect()
cur = conn.cursor()

cur.execute("CREATE TABLE people(person_id INT PRIMARY KEY, person_name VARCHAR NOT NULL)")
for person_id in range(0,2000):
    cur.execute(
        "INSERT INTO people(person_id, person_name) VALUES(%s, %s)",
        (
            person_id,
            "Vallery (Universe # %s)" % person_id
        )
    )
conn.commit()
