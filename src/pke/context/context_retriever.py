class ContextRetriever:



    def retrieve(
        self,
        ranked,
        max_items=None
    ):


        if max_items is None:

            return ranked



        return ranked[:max_items]