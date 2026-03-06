from .connector import PostgresConnector


class ConnectorFactory:

    @staticmethod
    def create_connector(connector_type: str):

        if connector_type == "postgres":
            return PostgresConnector()

        else:
            raise ValueError(f"Unsupported connector type: {connector_type}")