from .package_metrics import PackageMetrics



class PackageCouplingAnalyzer:



    def analyze(
        self,
        project
    ):


        packages = {}



        #
        # crea metriche
        #
        for package in project.packages:


            packages[
                package.name
            ] = PackageMetrics(
                name=package.name
            )



        #
        # costruisce indice funzione -> package
        #
        function_package = {}



        for package in project.packages:


            for file in package.files:


                for function in file.symbols:


                    function_package[
                        function.name
                    ] = package.name



        #
        # analizza chiamate
        #
        for package in project.packages:


            current = packages[
                package.name
            ]



            for file in package.files:


                for function in file.symbols:



                    for call in function.calls:


                        target = self._extract_target(
                            call
                        )



                        if target in function_package:


                            target_package = function_package[target]



                            if target_package != package.name:


                                if target_package not in current.dependencies:

                                    current.dependencies.append(
                                        target_package
                                    )



                                if package.name not in packages[target_package].dependents:

                                    packages[target_package].dependents.append(
                                        package.name
                                    )



        #
        # metriche
        #
        for metric in packages.values():


            metric.fan_out = len(
                metric.dependencies
            )


            metric.fan_in = len(
                metric.dependents
            )


            total = (
                metric.fan_in
                +
                metric.fan_out
            )


            if total > 0:

                metric.instability = (
                    metric.fan_out
                    /
                    total
                )


            else:

                metric.instability = 0.0



        return packages



    def _extract_target(
        self,
        call
    ):

        if "(" in call:

            return call.split("(")[0]


        return call