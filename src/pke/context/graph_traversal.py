import heapq



class GraphTraversal:


    def walk(
        self,
        graph,
        start,
        depth=1
    ):


        visited = []


        queue = [

            (
                0,
                start,
                0
            )

        ]


        seen = {}



        while queue:


            cost, node, level = heapq.heappop(
                queue
            )



            if node in seen:

                continue



            seen[node] = cost


            visited.append(
                node
            )



            if level >= depth:

                continue



            relations = graph.get_weighted_relations(
                node
            )


            for target, weight, relation in relations:


                if target not in seen:


                    heapq.heappush(

                        queue,

                        (

                            cost + weight,

                            target,

                            level + 1

                        )

                    )



        return visited