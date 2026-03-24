from etl.loaders.opensearch_indexer import OpenSearchIndexer
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
if not logger.handlers:
    ch = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

class LoaderFactory:
    @staticmethod
    def create_loader(loader_type: str):
        logger.info(f"Creating loader: {loader_type}")
        if loader_type == "opensearch":
            return OpenSearchIndexer()
        logger.error(f"Unknown loader type: {loader_type}")
        raise ValueError(f"Unknown loader type: {loader_type}")