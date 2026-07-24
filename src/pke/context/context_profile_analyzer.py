from .context_profile import ContextProfile



class ContextProfileAnalyzer:



    def analyze(
        self,
        task
    ):


        task = (
            task or ""
        ).lower()



        #
        # Debug
        #

        if any(

            word in task

            for word in [

                "fix",

                "bug",

                "errore",

                "error",

                "issue",

                "debug",

                "problema"

            ]

        ):


            return ContextProfile(

                name="debug",

                expand_callers=True,

                expand_dependencies=True,

                include_side_effects=True,

                max_depth=3,

                prioritize_risks=True,

                prioritize_callers=True,

                compression_mode="technical",

                detail_level="high"

            )



        #
        # Explain
        #

        if any(

            word in task

            for word in [

                "explain",

                "describe",

                "spiega",

                "analizza"

            ]

        ):


            return ContextProfile(

                name="explain",

                expand_dependencies=True,

                include_docs=True,

                include_side_effects=True,

                max_depth=2,

                compression_mode="semantic",

                detail_level="high"

            )



        #
        # Security
        #

        if any(

            word in task

            for word in [

                "security",

                "secure",

                "audit",

                "vulnerability",

                "cve",

                "permission",

                "auth",

                "authentication"

            ]

        ):


            return ContextProfile(

                name="security",

                expand_dependencies=True,

                expand_callers=True,

                include_side_effects=True,

                max_depth=3,

                prioritize_risks=True,

                prioritize_dependencies=True,

                compression_mode="security",

                detail_level="high"

            )



        #
        # Refactor
        #

        if any(

            word in task

            for word in [

                "refactor",

                "rename",

                "move",

                "extract"

            ]

        ):


            return ContextProfile(

                name="refactor",

                expand_callers=True,

                expand_dependencies=True,

                include_tests=True,

                max_depth=2,

                prioritize_dependencies=True,

                compression_mode="structural",

                detail_level="normal"

            )



        #
        # Default
        #

        return ContextProfile(

            name="default"

        )