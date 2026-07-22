from pathlib import Path

from .function_writer import FunctionWriter
from .file_writer import FileWriter
from .package_writer import PackageWriter
from .project_writer import ProjectWriter
from .architecture_metrics import ArchitectureMetrics



class KnowledgeGenerator:


    def __init__(
        self,
        output_path
    ):

        self.output_path = Path(
            output_path
        )



    def generate(
        self,
        project,
        call_graph=None
    ):

        metrics = {}


        if call_graph is not None:

            metrics = ArchitectureMetrics(
                call_graph
            ).calculate()



        project_path = (
            self.output_path
            /
            project.name
        )


        project_path.mkdir(
            parents=True,
            exist_ok=True
        )


        #
        # Project.md
        #
        ProjectWriter(
            project_path
        ).write(
            project,
            call_graph
        )



        for package in project.packages:


            package_path = (
                project_path
                /
                package.name
            )


            package_path.mkdir(
                parents=True,
                exist_ok=True
            )


            PackageWriter(
                package_path
            ).write(
                package
            )



            for file in package.files:


                file_path = (
                    package_path
                    /
                    file.name
                )


                file_path.mkdir(
                    parents=True,
                    exist_ok=True
                )


                FileWriter(
                    file_path
                ).write(
                    file
                )



                for symbol in file.symbols:

                    metric = metrics.get(
                        symbol.name
                    )


                    FunctionWriter(
                        file_path
                    ).write(
                        symbol,
                        metric
                    )