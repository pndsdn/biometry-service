import psycopg2
from psycopg2.extensions import AsIs

conn = psycopg2.connect(database="bio-tracking",
                        user="dbadmin",
                        password="pass",
                        host="postgres",
                        port="5432")

cursor = conn.cursor()


def insert(data: dict, file_name: str):
    name = file_name.split('.')
    file_name = "_".join(name)
    for key in data:
        query = "CREATE TABLE IF NOT EXISTS service.%s (id SERIAL NOT NULL, frame_id VARCHAR NOT NULL, obj_class VARCHAR NOT NULL, time VARCHAR NOT NULL);"
        cursor.execute(query, (AsIs(file_name),))
        cursor.execute("INSERT INTO service.%s (frame_id, obj_class, time) "
                       "VALUES (%s, %s, %s);", (AsIs(file_name),data[key][0], data[key][1], f'{round(float(data[key][2] / 30), 2)}s'))
        conn.commit()
