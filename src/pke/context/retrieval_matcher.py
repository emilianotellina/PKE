from pke.knowledge.retrieval_context import RetrievalContext



class RetrievalMatcher:



    def score(
        self,
        symbol,
        documents
    ):


        if not documents:

            return 0



        name = getattr(
            symbol,
            "name",
            str(symbol)
        )


        tokens = self._tokens(
            name
        )


        best = 0



        iterable = documents

        scores = None

        semantic_symbols = []



        if isinstance(
            documents,
            RetrievalContext
        ):

            iterable = documents.documents

            scores = documents.scores

            semantic_symbols = getattr(
                documents,
                "symbols",
                []
            )



        #
        # match semantico sugli symbols estratti
        #

        for semantic_symbol in semantic_symbols:


            semantic_tokens = self._tokens(
                semantic_symbol
            )


            match = self._match(
                tokens,
                semantic_tokens
            )


            if match:

                best = max(
                    best,
                    match + 5
                )



        #
        # match contenuto documenti
        #

        for index, document in enumerate(iterable):


            content = self._content(
                document
            )


            document_tokens = self._tokens(
                content
            )


            match = self._match(
                tokens,
                document_tokens
            )


            if match == 0:

                continue



            retrieval_score = 1


            if scores and index < len(scores):

                retrieval_score = max(
                    1,
                    scores[index]
                )



            value = match + retrieval_score



            if value > best:

                best = value



        return best



    def _match(
        self,
        symbol_tokens,
        document_tokens
    ):


        if not symbol_tokens:

            return 0



        common = (

            symbol_tokens

            &

            document_tokens

        )



        if not common:

            return 0



        return len(
            common
        )



    def _content(
        self,
        document
    ):


        if isinstance(
            document,
            dict
        ):

            return " ".join(

                str(value)

                for value

                in document.values()

            )



        return str(
            document
        )



    def _tokens(
        self,
        value
    ):


        value = str(
            value
        )


        value = value.replace(
            "_",
            " "
        )


        value = value.replace(
            ".",
            " "
        )


        value = value.replace(
            "/",
            " "
        )



        import re


        value = re.sub(
            r"([a-z0-9])([A-Z])",
            r"\1 \2",
            value
        )



        return set(

            token.lower()

            for token

            in value.split()

            if token

        )