from .symbol_reference import SymbolReference



class SymbolReferenceBuilder:


    def build(
        self,
        project
    ):

        references = {}



        #
        # Creazione indice funzioni
        #
        for package in project.packages:

            for file in package.files:

                for function in file.symbols:

                    references[
                        function.name
                    ] = SymbolReference(
                        name=function.name
                    )



        #
        # Analisi relazioni
        #
        for package in project.packages:

            for file in package.files:

                for function in file.symbols:


                    current = references[
                        function.name
                    ]



                    for call in function.calls:


                        if call not in current.calls:

                            current.calls.append(
                                call
                            )



                        target = self._target_name(
                            call
                        )



                        if target not in current.references:

                            current.references.append(
                                target
                            )



                        #
                        # chiamata interna
                        #
                        if target in references:


                            if function.name not in references[target].called_by:

                                references[target].called_by.append(
                                    function.name
                                )



        return references



    def _target_name(
        self,
        call
    ):

        if "(" in call:

            return call.split(
                "("
            )[0]

        return call