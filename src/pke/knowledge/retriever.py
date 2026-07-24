from .retrieval_context import RetrievalContext



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


        context = RetrievalContext(
            query=query
        )


        for item in results[:self.max_results]:

            context.add(

                item,

                score=item.get(
                    "score"
                )
                if isinstance(
                    item,
                    dict
                )
                else None,

                source=item.get(
                    "source"
                )
                if isinstance(
                    item,
                    dict
                )
                else None

            )


        return context



    def retrieve_content(
        self,
        query
    ):


        context = self.retrieve(
            query
        )


        return [

            item["content"]

            for item

            in context.documents

            if isinstance(
                item,
                dict
            )

            and

            "content" in item

        ]