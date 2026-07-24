from collections import deque



class ImpactAnalyzer:



    def analyze(
        self,
        graph,
        target
    ):


        if not graph.contains(
            target
        ):

            return {

                "target": target,

                "affected": [],

                "paths": [],

                "risk_level": "low"

            }



        affected = []

        paths = []



        queue = deque(

            [

                (

                    target,

                    [target]

                )

            ]

        )


        visited = set()



        while queue:


            current, path = queue.popleft()



            if current in visited:

                continue



            visited.add(
                current
            )



            relations = graph.nodes[current].relations



            for relation in (

                "called_by",

                "depends_on"

            ):


                for node in relations.get(
                    relation,
                    []
                ):


                    if node not in affected:

                        affected.append(
                            node
                        )


                    paths.append(
                        path + [node]
                    )


                    queue.append(
                        (
                            node,
                            path + [node]
                        )
                    )



        return {

            "target": target,

            "affected": affected,

            "paths": paths,

            "risk_level": self._risk_level(
                len(affected)
            )

        }



    def _risk_level(
        self,
        count
    ):


        if count == 0:

            return "low"



        if count <= 3:

            return "medium"



        return "high"