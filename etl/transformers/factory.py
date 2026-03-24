from etl.transformers.json_transformer import JSONTransformer
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
if not logger.handlers:
    ch = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

class TransformerFactory:
    @staticmethod
    def create_transformer(transformer_type: str):
        logger.info(f"Creating transformer: {transformer_type}")
        if transformer_type == "json":
            return JSONTransformer()
        logger.error(f"Unknown transformer type: {transformer_type}")
        raise ValueError(f"Unknown transformer type: {transformer_type}")