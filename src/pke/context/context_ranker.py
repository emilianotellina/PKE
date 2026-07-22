from .context import SymbolContext



class ContextRanker:



    def rank(
        self,
        context,
        target
    ):


        result = []


        target_symbol = None


        for symbol in context.symbols:

            if symbol.name == target:

                target_symbol = symbol

                break



        if target_symbol is None:

            return result



        #
        # Target principale
        #

        result.append(
            (
                target_symbol,
                100
            )
        )



        #
        # Caller
        #

        for symbol in context.symbols:


            for call in symbol.calls:


                called_name = call.split("(")[0]


                if called_name == target:


                    result.append(
                        (
                            symbol,
                            80
                        )
                    )


        #
        # Dependencies
        #

        for dependency in target_symbol.dependencies:


            result.append(
                (
                    dependency,
                    70
                )
            )



        #
        # Side effects
        #

        if target_symbol.side_effects:


            result.append(
                (
                    target_symbol,
                    60
                )
            )



        #
        # Remove duplicati
        #

        unique = []

        seen = set()


        for item,score in result:


            key = (
                getattr(item, "name", str(item)),
                score
            )


            if key not in seen:

                seen.add(key)

                unique.append(
                    (
                        item,
                        score
                    )
                )



        unique.sort(
            key=lambda x:x[1],
            reverse=True
        )


        return unique