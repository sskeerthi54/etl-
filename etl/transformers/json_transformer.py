import pandas as pd


class JSONTransformer:
    """
    Pure transformer:
    - Takes ANY structured input
    - Converts to clean JSON dictionary
    - No DB connection
    - No embedding logic
    """

    def transform(self, data):
        # -------------------------------
        # Step 1: Normalize input → list of dicts
        # -------------------------------
        if isinstance(data, pd.DataFrame):
            clean_list = data.to_dict(orient="records")

        elif isinstance(data, (list, tuple)):
            if len(data) == 0:
                return {}

            # Already list of dicts
            if isinstance(data[0], dict):
                clean_list = data
            else:
                # Assume tuple structure → (id, name, email)
                keys = ["student_id", "name", "department", "marks"]
                clean_list = [dict(zip(keys, row)) for row in data]

        else:
            raise TypeError("Unsupported data type for transformation")

        # -------------------------------
        # Step 2: Convert → JSON dictionary
        # Format: {id: {name, email}}
        # -------------------------------
        result = {
            item["student_id"]: {
                "name": item["name"],
                "department": item["department"],
                "marks":item["marks"]
            }
            for item in clean_list
        }

        return result