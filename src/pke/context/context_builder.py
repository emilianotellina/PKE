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



        metrics_index = {}

        if metrics:

            for name, value in metrics.items():

                metrics_index[name] = value



        call_index = {}

        if call_graph:


            for name, node in call_graph.nodes.items():

                call_index[name] = node



        for package in project.packages:


            for file in package.files:


                for function in file.symbols:


                    symbol = SymbolContext(
                        name=function.name
                    )



                    #
                    # chiamate dirette
                    #

                    symbol.calls.extend(
                        function.calls
                    )



                    #
                    # target risolti
                    #

                    if hasattr(
                        function,
                        "call_targets"
                    ):

                        symbol.calls.extend(
                            function.call_targets
                        )



                    #
                    # chiamatori
                    #

                    if function.name in call_index:


                        node = call_index[
                            function.name
                        ]


                        if hasattr(
                            node,
                            "callers"
                        ):

                            symbol.called_by.extend(
                                node.callers
                            )



                    #
                    # chiamatori dal modello knowledge
                    #

                    if hasattr(
                        function,
                        "called_by"
                    ):

                        symbol.called_by.extend(
                            function.called_by
                        )



                    #
                    # side effects
                    #

                    symbol.side_effects.extend(

                        [
                            effect.type

                            for effect

                            in function.side_effects

                        ]

                    )



                    #
                    # dependencies
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



                    #
                    # metadata architetturale
                    #

                    symbol.metrics.update(

                        {

                            "package":
                                package.name,

                            "file":
                                file.name

                        }

                    )



                    context.symbols.append(
                        symbol
                    )



        context.architecture = {

            "packages":

                len(project.packages),


            "files":

                sum(

                    len(package.files)

                    for package in project.packages

                ),


            "functions":

                len(context.symbols)

        }



        return context