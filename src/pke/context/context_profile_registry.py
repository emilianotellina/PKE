from .context_profile import ContextProfile



class ContextProfileRegistry:



    def __init__(
        self
    ):

        self.profiles = {

            "default":
                ContextProfile(

                    name="default"

                ),


            "debug":
                ContextProfile(

                    name="debug",

                    expand_callers=True,

                    expand_dependencies=True,

                    include_side_effects=True,

                    max_depth=3,

                    prioritize_risks=True,

                    prioritize_callers=True,

                    compression_mode="technical",

                    detail_level="high"

                ),


            "security":
                ContextProfile(

                    name="security",

                    expand_dependencies=True,

                    expand_callers=True,

                    include_side_effects=True,

                    max_depth=3,

                    prioritize_risks=True,

                    prioritize_dependencies=True,

                    compression_mode="security",

                    detail_level="high"

                ),


            "refactor":
                ContextProfile(

                    name="refactor",

                    expand_callers=True,

                    expand_dependencies=True,

                    include_tests=True,

                    max_depth=2,

                    prioritize_dependencies=True,

                    compression_mode="structural",

                    detail_level="normal"

                ),


            "explain":
                ContextProfile(

                    name="explain",

                    expand_dependencies=True,

                    include_docs=True,

                    include_side_effects=True,

                    max_depth=2,

                    compression_mode="semantic",

                    detail_level="high"

                )

        }



    def get(
        self,
        name
    ):

        return self.profiles.get(

            name,

            self.profiles["default"]

        )



    def register(
        self,
        profile
    ):

        self.profiles[

            profile.name

        ] = profile



    def contains(
        self,
        name
    ):

        return name in self.profiles



    def list(
        self
    ):

        return list(

            self.profiles.values()

        )