import database

import time
import sys


def build_query(ids):
    sql = "SELECT * FROM people WHERE person_id IN (%s)" % ", ".join(ids)

    results = database.select(sql, ids)
    print(results)


start_time = time.time()
build_query(sys.argv[1:])
end_time = time.time()

print(end_time - start_time)