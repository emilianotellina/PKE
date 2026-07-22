from .context import (
    AIContext,
    SymbolContext,
)



class ContextBuilder:



    def build(
        self,
        project,
        call_graph=None,
        dependency_graph=None,
        metrics=None
    ):


        context = AIContext(
            project=project.name
        )



        #
        # indice metriche
        #

        metrics_index = {}

        if metrics:

            for name,value in metrics.items():

                metrics_index[name] = value



        #
        # indice call graph
        #

        call_index = {}

        if call_graph:


            for name,node in call_graph.nodes.items():

                call_index[name] = node



        #
        # costruzione simboli
        #

        for package in project.packages:


            for file in package.files:


                for function in file.symbols:


                    symbol = SymbolContext(
                        name=function.name
                    )



                    #
                    # chiamate
                    #

                    symbol.calls.extend(
                        function.calls
                    )



                    #
                    # chiamato da
                    #

                    if function.name in call_index:


                        symbol.called_by.extend(
                            call_index[
                                function.name
                            ].callers
                        )



                    #
                    # effetti
                    #

                    symbol.side_effects.extend(
                        [
                            effect.type
                            for effect
                            in function.side_effects
                        ]
                    )



                    #
                    # dipendenze
                    #

                    symbol.dependencies.extend(
                        [
                            dependency.type
                            for dependency
                            in function.dependencies
                        ]
                    )



                    #
                    # metriche
                    #

                    if function.name in metrics_index:

                        metric = metrics_index[
                            function.name
                        ]


                        symbol.metrics = {

                            "fan_in":
                                metric.fan_in,

                            "fan_out":
                                metric.fan_out,

                            "complexity":
                                metric.complexity,

                            "criticality":
                                metric.criticality

                        }



                    context.symbols.append(
                        symbol
                    )



        #
        # statistiche progetto
        #

        context.architecture = {

            "packages":
                len(project.packages),

            "files":
                sum(
                    len(p.files)
                    for p in project.packages
                ),

            "functions":
                len(context.symbols)

        }



        return context