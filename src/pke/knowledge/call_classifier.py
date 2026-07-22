class CallClassifier:


    BUILTINS = {
        "print",
        "len",
        "range",
        "str",
        "int",
        "float"
    }



    def classify(
        self,
        call,
        project_functions
    ):

        target = call.target


        if target in project_functions:

            return "internal"


        if target in self.BUILTINS:

            return "builtin"


        return "external"