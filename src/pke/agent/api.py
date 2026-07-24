from .query import query
from .protocol import AgentResponse
from .errors import AgentError, AgentErrorResponse
from .query_router import QueryRouter
from .candidate import QueryCandidate
from .context_cache import ContextCache

from pke.context.agent_selector import AgentSelector



class AgentAPI:


    def __init__(
        self,
        project,
        profile=None
    ):

        self.project = project

        self.profile = profile

        self.router = QueryRouter()

        self.cache = ContextCache()

        self.agent_selector = AgentSelector()



    def _target_exists(
        self,
        target
    ):

        return bool(
            self.router.find_symbol(
                self.project,
                target
            )
        )



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



    def _resolve_agent(
        self,
        task
    ):

        return self.agent_selector.select(
            task
        )



    def _apply_profile(
        self,
        options,
        agent
    ):

        options = dict(
            options or {}
        )


        if "profile" not in options:

            if self.profile is not None:

                options["profile"] = self.profile


            elif agent is not None:

                options["profile"] = agent.context_profile


        return options



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



        agent = self._resolve_agent(
            task
        )


        options = self._apply_profile(
            options,
            agent
        )


        candidates = self.router.route(
            self.project,
            task
        )



        if target is None and candidates:

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

            agent=(

                agent.name
                if agent
                else None

            ),

            profile=(

                agent.context_profile.name
                if agent
                else None

            ),

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

        return self.query(
            task,
            target,
            options
        ).to_json()