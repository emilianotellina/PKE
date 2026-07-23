from .api import AgentAPI
from .errors import AgentError, AgentErrorResponse
from .request import AgentRequest
from .context_cache import ContextCache
from .project_fingerprint import ProjectFingerprint



class PKEAgentAdapter:


    def __init__(
        self,
        project
    ):

        self.project = project

        self.api = AgentAPI(
            project
        )

        self.cache = ContextCache()

        self.fingerprint = ProjectFingerprint()



    def handle(
        self,
        request
    ):


        if not isinstance(
            request,
            dict
        ):

            return AgentErrorResponse(

                AgentError(
                    "INVALID_REQUEST",
                    "Request must be a dictionary"
                )

            )



        agent_request = AgentRequest.from_dict(
            request
        )



        fingerprint = self.fingerprint.calculate(
            self.project
        )



        cached = self.cache.get(

            fingerprint,

            agent_request.task,

            agent_request.target,

            agent_request.options

        )


        if cached is not None:

            return cached



        response = self.api.query(

            task=agent_request.task,

            target=agent_request.target,

            options=agent_request.options

        )



        self.cache.put(

            fingerprint,

            agent_request.task,

            agent_request.target,

            agent_request.options,

            response

        )



        return response



    def handle_json(
        self,
        request
    ):


        response = self.handle(
            request
        )


        if hasattr(
            response,
            "to_json"
        ):

            return response.to_json()



        import json


        return json.dumps(

            response.to_dict(),

            indent=2

        )