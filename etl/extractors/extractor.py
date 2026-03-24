from etl.connectors.connector import get_postgres_connection
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
if not logger.handlers:
    ch = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

class PatientExtractor:
    def extract(self):
        logger.info("Starting data extraction from PostgreSQL")
        conn = get_postgres_connection()
        try:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT 
                        id, name, age, gender, blood_type,
                        medical_condition, date_of_admission,
                        doctor, hospital, insurance_provider,
                        billing_amount, room_number,
                        admission_type, discharge_date,
                        medication, test_result
                    FROM patients;
                """)
                rows = cur.fetchall()
                logger.info(f"Extracted {len(rows)} records")
                return rows
        finally:
            conn.close()
            logger.info("PostgreSQL connection closed")