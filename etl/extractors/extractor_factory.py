from .extractor import DataExtractor


class ExtractorFactory:

    @staticmethod
    def create_extractor(extractor_type: str, connection):

        if extractor_type == "postgres":
            return DataExtractor(connection)

        else:
            raise ValueError(f"Unsupported extractor type: {extractor_type}")