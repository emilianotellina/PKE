from .agent_profile import AgentProfile
from .context_profile_registry import ContextProfileRegistry



class AgentRegistry:



    def __init__(
        self
    ):

        self.profile_registry = ContextProfileRegistry()


        self.agents = {


            "default":

                AgentProfile(

                    name="default",

                    description=
                        "General purpose analysis agent",

                    context_profile=
                        self.profile_registry.get(
                            "default"
                        )

                ),



            "debug":

                AgentProfile(

                    name="debug",

                    description=
                        "Agent specialized in debugging and error analysis",

                    context_profile=
                        self.profile_registry.get(
                            "debug"
                        ),

                    capabilities=[

                        "bug_analysis",

                        "risk_analysis",

                        "caller_analysis"

                    ]

                ),



            "security":

                AgentProfile(

                    name="security",

                    description=
                        "Agent specialized in security analysis",

                    context_profile=
                        self.profile_registry.get(
                            "security"
                        ),

                    capabilities=[

                        "risk_analysis",

                        "dependency_analysis",

                        "vulnerability_detection"

                    ]

                ),



            "refactor":

                AgentProfile(

                    name="refactor",

                    description=
                        "Agent specialized in refactoring analysis",

                    context_profile=
                        self.profile_registry.get(
                            "refactor"
                        ),

                    capabilities=[

                        "dependency_analysis",

                        "structural_analysis",

                        "caller_analysis"

                    ]

                ),



            "explain":

                AgentProfile(

                    name="explain",

                    description=
                        "Agent specialized in explanation and documentation",

                    context_profile=
                        self.profile_registry.get(
                            "explain"
                        ),

                    capabilities=[

                        "documentation_analysis",

                        "semantic_analysis"

                    ]

                )

        }



    def register(
        self,
        agent
    ):

        self.agents[

            agent.name

        ] = agent



    def get(
        self,
        name
    ):

        return self.agents.get(
            name
        )



    def contains(
        self,
        name
    ):

        return name in self.agents



    def list(
        self
    ):

        return list(

            self.agents.values()

        )