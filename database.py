import psycopg2 as pg

import config


def connect():
    return pg.connect(
        "host=%s dbname=%s user=%s password=%s" % (config.db_host, config.db_name, config.db_user, config.db_password)
    )


def select(sql, params):
    conn = connect()
    cur = conn.cursor()
    cur.execute(sql, params)
    return cur.fetchall()
