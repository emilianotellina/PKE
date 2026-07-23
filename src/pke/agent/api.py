from .query import query
from .protocol import AgentResponse
from .errors import AgentError, AgentErrorResponse
from .query_router import QueryRouter
from .candidate import QueryCandidate
from .context_cache import ContextCache



class AgentAPI:


    def __init__(
        self,
        project
    ):

        self.project = project

        self.router = QueryRouter()

        self.cache = ContextCache()



    def _target_exists(
        self,
        target
    ):

        return len(
            self.router.find_symbol(
                self.project,
                target
            )
        ) > 0



    def _validate(
        self,
        task,
        target
    ):

        if not task:

            return AgentErrorResponse(

                AgentError(
                    "TASK_REQUIRED",
                    "Task is required"
                )

            )


        if target and not self._target_exists(target):

            return AgentErrorResponse(

                AgentError(
                    "TARGET_NOT_FOUND",
                    f"Function {target} not found"
                )

            )


        return None



    def query(
        self,
        task,
        target=None,
        options=None
    ):


        error = self._validate(
            task,
            target
        )


        if error:

            return error



        candidates = self.router.route(
            self.project,
            task
        )



        if target is None:


            if not candidates:

                return AgentErrorResponse(

                    AgentError(
                        "TARGET_NOT_FOUND",
                        "No matching target found"
                    )

                )


            target = candidates[0]["symbol"]



        result = query(

            self.project,

            task,

            target,

            options,

            cache=self.cache

        )



        return AgentResponse(

            task=result.task,

            target=result.target,

            context=result.context,

            candidates=[

                QueryCandidate(

                    symbol=item["symbol"],

                    score=item["score"]

                )

                for item in candidates

            ],

            functions=result.functions,

            files=result.files,

            packages=result.packages,

            dependencies=result.dependencies,

            side_effects=result.side_effects,

            risks=result.risks,

            impact=result.impact

        )



    def query_json(
        self,
        task,
        target=None,
        options=None
    ):

        response = self.query(
            task,
            target,
            options
        )


        return response.to_json()