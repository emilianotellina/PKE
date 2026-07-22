class CallResolver:


    INTERNAL = "internal"

    EXTERNAL = "external"

    BUILTIN = "builtin"



    def __init__(
        self,
        functions
    ):

        self.functions = {
            function.name
            for function in functions
        }



    def resolve(
        self,
        call
    ):

        #
        # chiamata funzione interna
        #
        if (
            not call.receiver
            and call.target in self.functions
        ):

            call.resolved_type = (
                self.INTERNAL
            )

            return call



        #
        # chiamata metodo di oggetto
        #
        if call.receiver:

            call.resolved_type = (
                self.EXTERNAL
            )

            call.module = (
                call.receiver
            )

            return call



        #
        # built-in Python
        #
        builtin = {
            "print",
            "len",
            "str",
            "int",
            "float",
            "list",
            "dict",
            "set",
        }


        if call.target in builtin:

            call.resolved_type = (
                self.BUILTIN
            )

            return call



        #
        # fallback
        #
        call.resolved_type = (
            self.EXTERNAL
        )

        return call