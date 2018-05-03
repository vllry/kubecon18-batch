This is a quick demo for "Challenges To Writing Cloud Native Applications", to highlight the speed of batch endpoints and queries.

Running
==

Run populate.py to write test data to the DB.

Running `main.py [id1] [id2] [...]` will select all the rows where person_id matches (0-1999). It uses a naive timing mechanism to display the request time.

Setup
==

Depends on Postgres, Python3, and the Python3 package for psycopg2 (`pip3 install psycopg2`).

If you have Docker Compose, there's a compose file that will handle the Postgres instance for you. The Python scripts can run locally.

config.py contains the environment variables needed to connect to Postgres. All but POSTGRES_PASSWORD are set to defaults for compose. Using `export POSTGRES_PASSWORD=` will set that.