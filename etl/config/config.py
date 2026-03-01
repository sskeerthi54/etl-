import os
from dotenv import load_dotenv
from pathlib import Path

# -------------------------------
# Load .env from project root
# -------------------------------
# Assuming this file is: etl/config/config.py
# .env is in project root (two levels up)
env_path = Path(__file__).resolve().parents[2] / ".env"
if not env_path.exists():
    raise FileNotFoundError(f".env file not found at {env_path}")

load_dotenv(dotenv_path=env_path)

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

# -------------------------------
# Check required values
# -------------------------------
missing = [k for k, v in DB_CONFIG.items() if not v] #[expression for item in iterable if condition]
if missing:
    raise RuntimeError(f"Missing database config in .env: {', '.join(missing)}") #["user", "password","port"]
