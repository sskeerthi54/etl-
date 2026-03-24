from etl.extractors.extractor import PatientExtractor
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
if not logger.handlers:
    ch = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

class ExtractorFactory:
    @staticmethod
    def create_extractor(extractor_type: str):
        logger.info(f"Creating extractor: {extractor_type}")
        if extractor_type == "patient":
            return PatientExtractor()
        logger.error(f"Unknown extractor type: {extractor_type}")
        raise ValueError(f"Unknown extractor type: {extractor_type}")