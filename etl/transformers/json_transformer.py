import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
if not logger.handlers:
    ch = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

class JSONTransformer:
    def transform(self, data):
        logger.info(f"Transforming {len(data)} records")
        keys = [
            "id","name","age","gender","blood_type",
            "medical_condition","date_of_admission",
            "doctor","hospital","insurance_provider",
            "billing_amount","room_number",
            "admission_type","discharge_date",
            "medication","test_result"
        ]
        clean_list = [dict(zip(keys, row)) for row in data]
        documents = []
        for item in clean_list:
            doc = {k: (str(v) if v is not None else "") for k, v in item.items()}
            doc["content"] = " ".join([
                str(item.get(f) or "") for f in [
                    "name","medical_condition","doctor","hospital",
                    "medication","test_result","blood_type","admission_type"
                ]
            ])
            documents.append(doc)
        logger.info("Transformation complete")
        return documents