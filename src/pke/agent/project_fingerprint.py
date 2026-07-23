import hashlib



class ProjectFingerprint:


    def calculate(
        self,
        project
    ):


        elements = []


        nodes = getattr(
            project,
            "nodes",
            []
        )


        for node in nodes:

            elements.append(
                self._serialize(node)
            )


        elements.sort()


        payload = "\n".join(
            elements
        )


        return hashlib.sha256(
            payload.encode("utf-8")
        ).hexdigest()



    def _serialize(
        self,
        node
    ):


        parts = []


        parts.append(
            str(
                getattr(
                    node,
                    "type",
                    ""
                )
            )
        )


        parts.append(
            str(
                getattr(
                    node,
                    "name",
                    ""
                )
            )
        )


        parts.append(
            str(
                getattr(
                    node,
                    "value",
                    ""
                )
            )
        )


        return "|".join(
            parts
        )