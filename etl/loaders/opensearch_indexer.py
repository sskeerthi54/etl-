from opensearchpy import OpenSearch
import uuid
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
if not logger.handlers:
    ch = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

class OpenSearchIndexer:
    def __init__(self, host="localhost", port=9200, index_name="patients",
                 username="admin", password="admin", use_ssl=False):
        self.index_name = index_name
        logger.info(f"Connecting to OpenSearch at {host}:{port}")
        self.client = OpenSearch(
            hosts=[{"host": host, "port": port}],
            http_auth=(username, password),
            use_ssl=use_ssl,
            verify_certs=False,
            timeout=30
        )
        logger.info("OpenSearch connection established")

    def create_index_if_not_exists(self):
        if not self.client.indices.exists(index=self.index_name):
            logger.info(f"Creating OpenSearch index: {self.index_name}")
            self.client.indices.create(
                index=self.index_name,
                body={
                    "mappings": {
                        "properties": {
                            "id": {"type": "integer"},
                            "name": {"type": "text"},
                            "age": {"type": "integer"},
                            "gender": {"type": "keyword"},
                            "blood_type": {"type": "keyword"},
                            "medical_condition": {"type": "text"},
                            "date_of_admission": {"type": "date"},
                            "doctor": {"type": "text"},
                            "hospital": {"type": "text"},
                            "insurance_provider": {"type": "text"},
                            "billing_amount": {"type": "float"},
                            "room_number": {"type": "integer"},
                            "admission_type": {"type": "keyword"},
                            "discharge_date": {"type": "date"},
                            "medication": {"type": "text"},
                            "test_result": {"type": "text"},
                            "content": {"type": "text"}
                        }
                    }
                }
            )

    def _normalize_doc(self, doc):
        if isinstance(doc, (list, tuple)):
            keys = [
                "id","name","age","gender","blood_type",
                "medical_condition","date_of_admission",
                "doctor","hospital","insurance_provider",
                "billing_amount","room_number",
                "admission_type","discharge_date",
                "medication","test_result"
            ]
            return dict(zip(keys, doc))
        if isinstance(doc, dict):
            return doc
        return {"content": str(doc)}

    def index_documents(self, documents: list):
        logger.info(f"Indexing {len(documents)} documents into OpenSearch")
        self.create_index_if_not_exists()
        bulk_body = []
        for doc in documents:
            clean_doc = self._normalize_doc(doc)
            bulk_body.append({"index": {"_index": self.index_name, "_id": str(uuid.uuid4())}})
            bulk_body.append(clean_doc)
        response = self.client.bulk(body=bulk_body)
        logger.info("Documents indexed successfully")
        return response.get('items', [])