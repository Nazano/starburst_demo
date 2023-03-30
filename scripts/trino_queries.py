"""Run queries against Trino
"""
from trino.dbapi import connect
import os
import json

def execute_queries(cur, queries):

    for query in queries:
        print("Computing queires . . .")
        cur.execute(query)
        cur.fetchall()
        print(json.dumps(cur.stats, sort_keys=True, indent=4))

if __name__ == "__main__":

    conn = connect(
        host=os.environ["TRINO_ADDRESS"],
        port=os.environ["TRINO_PORT"],
        user=os.environ["TRINO_USER"],
    )

    cur = conn.cursor()

# Since we don't have any common PK values in both columns, the result is empty
    QUERY1 = "SELECT r.numvotes, b.originaltitle\
                FROM mysql.films.ratings r\
                JOIN mongodb.films.basics b\
                ON r.tconst = b.tconst"

# Join same table from each datastore
    QUERY2 = "SELECT r.genres, b.genres , COUNT(*) AS nbFilms\
                FROM mysql.films.basics r\
                LEFT JOIN mongodb.films.basics b\
                ON r.genres = b.genres\
                GROUP BY (r.genres, b.genres)"
    
# Join tables with common column and no PK with the USING keyword 
    QUERY3 = "SELECT * \
                FROM mysql.films.basics \
                LEFT JOIN mongodb.films.basics \
                USING (genres)"
    
# Cross Join = Cartesian Product of tables from each datastore
    QUERY4 = "SELECT * FROM mysql.films.basics, mongodb.films.basics"

# Append rows alongside of each datastore with UNION
    QUERY5 = "SELECT myb.originaltitle\
                FROM mysql.films.basics myb\
                UNION\
                SELECT mob.originaltitle\
                FROM mongodb.films.basics mob"
    
# Count the rows of the previous query 
    QUERY6 = "SELECT COUNT(*) FROM ( \
                SELECT myb.originaltitle\
                FROM mysql.films.basics myb\
                UNION\
                SELECT mob.originaltitle\
                FROM mongodb.films.basics mob)"

    queries = [QUERY1, QUERY2, QUERY3, QUERY4, QUERY5, QUERY6]

    execute_queries(cur, queries)
    print("Queries done")