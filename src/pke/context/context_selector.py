class ContextSelector:


    def select(
        self,
        ranked_context,
        limit=None,
        min_score=None
    ):

        selected = []


        for item, score in ranked_context:


            if (
                min_score is not None
                and score < min_score
            ):

                continue


            selected.append(
                (
                    item,
                    score
                )
            )


            if (
                limit is not None
                and len(selected) >= limit
            ):

                break


        return selected