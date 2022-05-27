import psycopg2

if __name__ == "__main__":
    conn = psycopg2.connect(database="bio-tracking",
                            user="dbadmin",
                            password="pass",
                            host="postgres",
                            port="5432")

    cursor = conn.cursor()
    query = """CREATE SCHEMA IF NOT EXISTS service AUTHORIZATION dbadmin;"""
    cursor.execute(query)
    conn.commit()
