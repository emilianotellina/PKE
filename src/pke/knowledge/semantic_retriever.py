class SemanticRetriever:



    def __init__(
        self,
        repository=None
    ):

        self.repository = repository



    def expand(
        self,
        retrieval_context
    ):


        if retrieval_context is None:

            return None



        documents = getattr(
            retrieval_context,
            "documents",
            []
        )



        symbols = []



        for document in documents:


            if isinstance(
                document,
                dict
            ):

                content = document.get(
                    "content",
                    ""
                )

            else:

                content = str(
                    document
                )



            symbols.extend(

                self._extract_symbols(
                    content
                )

            )



        retrieval_context.symbols = list(

            dict.fromkeys(
                symbols
            )

        )



        return retrieval_context



    def _extract_symbols(
        self,
        content
    ):


        result = []



        for line in content.splitlines():


            line = line.strip()



            if line.startswith(
                "# Function:"
            ):

                result.append(

                    line.replace(
                        "# Function:",
                        ""
                    ).strip()

                )



            elif line.startswith(
                "- "
            ):

                value = line[2:].strip()



                if value:

                    result.append(
                        value
                    )



        return result