import psycopg2

if __name__ == "__main__":
    conn = psycopg2.connect(database="bio-tracking",
                            user="dbadmin",
                            password="pass",
                            host="postgres",
                            port="5432")

    cursor = conn.cursor()

    query = """
CREATE SCHEMA IF NOT EXISTS service AUTHORIZATION dbadmin;
CREATE TABLE IF NOT EXISTS service.objects (id SERIAL NOT NULL, frame_id VARCHAR NOT NULL, obj_class VARCHAR NOT NULL, time VARCHAR NOT NULL);
"""
    cursor.execute(query)
    conn.commit()
