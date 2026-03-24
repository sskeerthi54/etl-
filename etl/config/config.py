import os
from dotenv import load_dotenv
from pathlib import Path
import logging

# -------------------------------
# Logger setup
# -------------------------------
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
if not logger.handlers:
    ch = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

# -------------------------------
# Load .env from project root
# -------------------------------
env_path = Path(__file__).resolve().parents[2] / ".env"
if not env_path.exists():
    logger.error(f".env file not found at {env_path}")
    raise FileNotFoundError(f".env file not found at {env_path}")

load_dotenv(dotenv_path=env_path)
logger.info(".env loaded successfully")

# -------------------------------
# Load DB configuration
# -------------------------------
DB_CONFIG = {
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST", "localhost"),
    "port": int(os.getenv("DB_PORT", 5432)),
}

missing = [k for k, v in DB_CONFIG.items() if not v]
if missing:
    logger.error(f"Missing database config in .env: {', '.join(missing)}")
    raise RuntimeError(f"Missing database config in .env: {', '.join(missing)}")

logger.info("Database configuration loaded successfully")