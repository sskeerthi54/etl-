from etl.connectors.connector import get_postgres_connection


class UserExtractor:
    def extract(self):
        conn = get_postgres_connection()
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT student_id, name, department, marks FROM students;")
                return cur.fetchall()
        finally:
            conn.close()