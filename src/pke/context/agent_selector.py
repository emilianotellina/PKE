from .agent_registry import AgentRegistry
from .agent_profile import AgentProfile
from .context_profile import ContextProfile



class AgentSelector:



    def __init__(
        self,
        registry=None
    ):

        self.registry = registry or AgentRegistry()



    def select(
        self,
        task
    ):


        task = (
            task or ""
        ).lower()



        #
        # Refactor
        # deve avere priorità su security
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

            return self.registry.get(
                "refactor"
            )



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
                "debug",
                "issue",
                "problema"

            ]

        ):

            return self.registry.get(
                "debug"
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
                "authentication"

            ]

        ):

            return self.registry.get(
                "security"
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

            return self.registry.get(
                "explain"
            )



        #
        # Default
        #

        default = self.registry.get(
            "default"
        )


        if default is not None:

            return default



        #
        # fallback nel caso registry custom
        #

        return AgentProfile(

            name="default",

            context_profile=ContextProfile(

                name="default"

            )

        )