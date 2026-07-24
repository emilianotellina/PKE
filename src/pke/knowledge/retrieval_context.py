from dataclasses import dataclass, field



@dataclass
class RetrievalContext:


    query: str


    documents: list = field(
        default_factory=list
    )


    scores: list = field(
        default_factory=list
    )


    sources: list = field(
        default_factory=list
    )



    def add(
        self,
        document,
        score=None,
        source=None
    ):

        self.documents.append(
            document
        )


        if score is not None:

            self.scores.append(
                score
            )


        if source is not None:

            self.sources.append(
                source
            )



    #
    # compatibilità lista
    #

    def __iter__(
        self
    ):

        return iter(
            self.documents
        )



    def __len__(
        self
    ):

        return len(
            self.documents
        )



    def __getitem__(
        self,
        index
    ):

        return self.documents[index]



    def names(
        self
    ):

        result = []


        for document in self.documents:


            if isinstance(
                document,
                dict
            ):

                result.append(

                    document.get(
                        "name",
                        document.get(
                            "path",
                            "unknown"
                        )
                    )

                )

            else:

                result.append(
                    str(document)
                )


        return result



    def to_dict(
        self
    ):

        return {

            "query":
                self.query,

            "documents":
                self.documents,

            "scores":
                self.scores,

            "sources":
                self.sources

        }