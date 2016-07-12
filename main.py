import os
import psycopg2
from urllib.parse import urlparse

url = urlparse(os.environ["DATABASE_URL"])
print(url)
conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)
cur = conn.cursor()
cur.execute("CREATE TABLE test2 (id serial PRIMARY KEY, num integer, data varchar);")
conn.commit()
cur.close()
conn.close()
