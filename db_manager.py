import psycopg2

conn = psycopg2.connect(database="bio-tracking",
                        user="dbadmin",
                        password="pass",
                        host="localhost",
                        port="5432")

cursor = conn.cursor()

cursor.execute("CREATE SCHEMA service;"
               "CREATE TABLE service.objects (id SERIAL NOT NULL, "
               "frame_id VARCHAR NOT NULL, "
               "class VARCHAR NOT NULL, "
               "time INT NOT NULL);")


def insert(data: dict):
    for i in data:
        cursor.execute("INSERT INTO public.test_bio (frame_id, class, time) "
                       "VALUES (%s, %s, %s);",
                       (str(data[i]), str(data[i][0]), float(data[i][1] / 30)))
