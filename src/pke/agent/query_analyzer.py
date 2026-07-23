class QueryAnalyzer:


    def analyze(
        self,
        project,
        target,
        call_graph=None
    ):

        result = {

            "functions": [],
            "files": [],
            "packages": [],
            "dependencies": [],
            "side_effects": [],
            "risks": []

        }


        if project is None:
            return result


        functions = self._find_functions(
            project,
            target
        )


        visited = set()


        for function in functions:

            self._analyze_function_tree(
                project,
                function,
                result,
                visited
            )


        return result



    def _find_functions(
        self,
        project,
        target
    ):

        found = []


        for package in project.packages:

            for file in package.files:

                for symbol in file.symbols:

                    if symbol.name == target:

                        found.append(
                            symbol
                        )


        return found



    def _analyze_function_tree(
        self,
        project,
        function,
        result,
        visited
    ):

        if function.name in visited:

            return


        visited.add(
            function.name
        )


        self._register_function(
            result,
            function
        )


        self._register_dependencies(
            result,
            function
        )


        self._register_side_effects(
            result,
            function
        )


        self._register_location(
            project,
            result,
            function
        )


        for target in function.call_targets:

            called = self._find_functions(
                project,
                target
            )


            for child in called:

                self._analyze_function_tree(
                    project,
                    child,
                    result,
                    visited
                )



    def _register_function(
        self,
        result,
        function
    ):

        if function.name not in result["functions"]:

            result["functions"].append(
                function.name
            )



    def _register_dependencies(
        self,
        result,
        function
    ):

        for dependency in function.dependencies:

            if dependency.type not in result["dependencies"]:

                result["dependencies"].append(
                    dependency.type
                )



    def _register_side_effects(
        self,
        result,
        function
    ):

        for effect in function.side_effects:

            if effect.type not in result["side_effects"]:

                result["side_effects"].append(
                    effect.type
                )



    def _register_location(
        self,
        project,
        result,
        function
    ):

        for package in project.packages:

            for file in package.files:

                if function in file.symbols:

                    if file.name not in result["files"]:

                        result["files"].append(
                            file.name
                        )


                    if package.name not in result["packages"]:

                        result["packages"].append(
                            package.name
                        )