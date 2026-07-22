from dataclasses import dataclass, field



@dataclass
class ArchitectureMap:


    packages: dict = field(
        default_factory=dict
    )



    def add_package(
        self,
        name
    ):

        if name not in self.packages:

            self.packages[name] = {
                "functions": []
            }


        return self.packages[name]