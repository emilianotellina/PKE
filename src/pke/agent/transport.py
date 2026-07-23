from .adapter import PKEAgentAdapter



class AgentTransport:


    def __init__(
        self,
        project
    ):

        self.adapter = PKEAgentAdapter(
            project
        )



    def process(
        self,
        payload: dict
    ):

        return self.adapter.handle(
            payload
        )



    def process_json(
        self,
        payload: dict
    ):

        return self.adapter.handle_json(
            payload
        )