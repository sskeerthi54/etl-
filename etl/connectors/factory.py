from etl.connectors.connector import get_postgres_connection
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
if not logger.handlers:
    ch = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

class ConnectorFactory:
    @staticmethod
    def create_connector(connector_type: str):
        logger.info(f"Creating connector: {connector_type}")
        if connector_type == "postgres":
            return get_postgres_connection
        logger.error(f"Unknown connector type: {connector_type}")
        raise ValueError(f"Unknown connector type: {connector_type}")