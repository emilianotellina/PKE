from .agent_selector import AgentSelector
from .context_profile_registry import ContextProfileRegistry



class ContextProfileSelector:


    def __init__(
        self
    ):

        self.registry = ContextProfileRegistry()

        self.agent_selector = AgentSelector(
            registry=self._build_agent_registry()
        )



    def _build_agent_registry(
        self
    ):

        return self.agent_selector_registry()



    def agent_selector_registry(
        self
    ):

        from .agent_registry import AgentRegistry

        return AgentRegistry()



    def select(
        self,
        task
    ):


        agent = self.agent_selector.select(
            task
        )


        if agent is None:

            return self.registry.get(
                "default"
            )


        return agent.context_profile