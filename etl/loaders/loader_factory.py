from .opensearch_indexer import OpenSearchIndexer


class LoaderFactory:

    @staticmethod
    def create_loader(loader_type: str):

        if loader_type == "opensearch":
            return OpenSearchIndexer()

        else:
            raise ValueError(f"Unsupported loader type: {loader_type}")