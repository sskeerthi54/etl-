from etl.extractors.factory import ExtractorFactory
from etl.transformers.factory import TransformerFactory
from etl.loaders.factory import LoaderFactory
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
if not logger.handlers:
    ch = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

class MedicalETLPipeline:
    def __init__(self):
        logger.info("Initializing Medical ETL Pipeline")
        self.extractor = ExtractorFactory.create_extractor("patient")
        self.transformer = TransformerFactory.create_transformer("json")
        self.loader = LoaderFactory.create_loader("opensearch")

    def run(self):
        try:
            rows = self.extractor.extract()
            logger.info(f"Extracted {len(rows)} rows")
            documents = self.transformer.transform(rows)
            logger.info(f"Transformed {len(documents)} documents")
            responses = self.loader.index_documents(documents)
            logger.info(f"Indexed {len(responses)} documents")
        except Exception as e:
            logger.error(f"Pipeline failed: {e}")
            raise
        logger.info("Pipeline finished successfully")