from opensearchpy import OpenSearch
import uuid


class OpenSearchIndexer:
    def __init__(self, host="localhost", port=9200, index_name="students"):
        # ✅ index name changed to students
        self.index_name = index_name

        self.client = OpenSearch(
            hosts=[{"host": host, "port": port}],
            http_compress=True
        )

    # ---------------------------------------------------
    # Create Index (only if not exists)
    # ---------------------------------------------------
    def create_index_if_not_exists(self):

        if not self.client.indices.exists(index=self.index_name):

            self.client.indices.create(
                index=self.index_name,
                body={
                    "mappings": {
                        "properties": {
                            "student_id": {"type": "integer"},
                            "name": {"type": "text"},
                            "department": {"type": "keyword"},
                            "marks": {"type": "integer"}
                        }
                    }
                }
            )

    # ---------------------------------------------------
    # Convert postgres row → JSON document
    # ---------------------------------------------------
    def _normalize_doc(self, doc):

        # postgres row tuple → structured JSON
        if isinstance(doc, (list, tuple)):
            return {
                "student_id": doc[0],
                "name": doc[1],
                "department": doc[2],
                "marks": doc[3],
            }

        # already dictionary
        if isinstance(doc, dict):
            return doc

        # fallback
        return {"content": str(doc)}

    # ---------------------------------------------------
    # Index Documents
    # ---------------------------------------------------
    def index_documents(self, documents: list):

        self.create_index_if_not_exists()

        responses = []

        for doc in documents:

            clean_doc = self._normalize_doc(doc)

            response = self.client.index(
                index=self.index_name,
                id=str(uuid.uuid4()),
                body=clean_doc
            )

            responses.append(response)

        return responses