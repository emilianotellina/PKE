from .project import Project
from .package import Package
from .file import SourceFile
from .function import Function



class KnowledgeProjectAdapter:


    def from_dict(
        self,
        data
    ):


        project = Project()

        project.name = data.get(
            "name",
            "unknown"
        )



        package_names = data.get(
            "packages",
            []
        )


        if package_names:

            package_name = package_names[0]

        else:

            package_name = "root"



        package = Package()

        package.name = package_name



        file_names = data.get(
            "files",
            []
        )


        if file_names:

            file_name = file_names[0]

        else:

            file_name = "unknown"



        source_file = SourceFile()

        source_file.name = file_name



        for function_name in data.get(
            "functions",
            []
        ):


            function = Function()

            function.name = function_name


            source_file.symbols.append(
                function
            )



        package.files.append(
            source_file
        )


        project.packages.append(
            package
        )


        return project