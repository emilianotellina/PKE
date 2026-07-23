class KnowledgeRetriever:


    def __init__(
        self,
        repository,
        max_results=5
    ):

        self.repository = repository

        self.max_results = max_results



    def retrieve(
        self,
        query
    ):


        results = self.repository.search(
            query
        )


        return results[
            :self.max_results
        ]



    def retrieve_content(
        self,
        query
    ):


        results = self.retrieve(
            query
        )


        return [

            item["content"]

            for item

            in results

        ]