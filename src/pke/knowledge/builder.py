from pathlib import Path

from pke.knowledge import (
    Project,
    Package,
    SourceFile,
    KnowledgeGraph,
)


class KnowledgeBuilder:


    def __init__(self):

        self.graph = KnowledgeGraph()



    def build_project(
        self,
        root,
        scanned_project
    ):

        project = Project(
            name=scanned_project.name,
            path=scanned_project.path
        )


        self.graph.add_node(
            project
        )


        for package in scanned_project.packages:

            self._add_package(
                project,
                package
            )


        return project



    def _add_package(
        self,
        project,
        package
    ):

        self.graph.add_node(
            package
        )


        self.graph.add_edge(
            project,
            package,
            "contains"
        )


        for file in package.files:

            self.graph.add_node(
                file
            )


            self.graph.add_edge(
                package,
                file,
                "contains"
            )