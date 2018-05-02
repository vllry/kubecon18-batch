import database

import sys


def build_query(ids):
    sql_base = "SELECT * FROM people WHERE "

    sql_where = []
    for _ in ids:
        sql_where.append("person_id = %s")

    sql = sql_base + " OR ".join(sql_where)

    results = database.select(sql, ids)
    print(results)


build_query(sys.argv[1:])
