import psycopg
from etl.config.config import DB_CONFIG
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
if not logger.handlers:
    ch = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

def get_postgres_connection():
    try:
        logger.info("Connecting to PostgreSQL...")
        conn = psycopg.connect(**DB_CONFIG)
        logger.info("PostgreSQL connection successful")
        return conn
    except Exception as e:
        logger.error(f"PostgreSQL connection failed: {e}")
        raise