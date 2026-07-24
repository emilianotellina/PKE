from dataclasses import dataclass

from .context_profile import ContextProfile



@dataclass
class ContextStrategy:


    expand_callers: bool = False

    expand_dependencies: bool = False

    include_tests: bool = False

    include_docs: bool = False

    include_side_effects: bool = False

    max_depth: int = 1





class ContextStrategyAnalyzer:



    def analyze(
        self,
        task
    ):


        task = (
            task or ""
        ).lower()



        strategy = ContextStrategy()



        if any(

            word in task

            for word in [

                "explain",

                "spiega",

                "analizza",

                "describe"

            ]

        ):


            strategy.include_docs = True

            strategy.expand_dependencies = True

            strategy.max_depth = 2



        if any(

            word in task

            for word in [

                "fix",

                "bug",

                "errore",

                "problema"

            ]

        ):


            strategy.expand_callers = True

            strategy.include_side_effects = True

            strategy.expand_dependencies = True

            strategy.max_depth = 3



        if any(

            word in task

            for word in [

                "rename",

                "refactor",

                "sposta",

                "move"

            ]

        ):


            strategy.expand_callers = True

            strategy.include_tests = True

            strategy.max_depth = 2



        if strategy.max_depth == 1:

            strategy.include_docs = True



        return strategy