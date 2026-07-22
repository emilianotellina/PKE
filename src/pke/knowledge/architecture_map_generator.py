from .architecture_map import ArchitectureMap



class ArchitectureMapGenerator:



    def generate(
        self,
        project
    ):


        architecture = ArchitectureMap()



        for package in project.packages:


            package_info = architecture.add_package(
                package.name
            )


            for file in package.files:


                for function in file.symbols:


                    data = {

                        "name": function.name,

                        "calls": list(
                            function.calls
                        ),

                        "effects": [
                            e.type
                            for e in function.side_effects
                        ],

                    }


                    package_info[
                        "functions"
                    ].append(
                        data
                    )



        return architecture