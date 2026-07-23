from dataclasses import dataclass, field



@dataclass
class ImpactReport:


    target: str | None


    callers: list[str] = field(
        default_factory=list
    )


    calls: list[str] = field(
        default_factory=list
    )


    dependencies: list[str] = field(
        default_factory=list
    )


    side_effects: list[str] = field(
        default_factory=list
    )


    complexity: float | None = None



    def to_dict(
        self
    ):

        return {

            "target":
                self.target,

            "callers":
                self.callers,

            "calls":
                self.calls,

            "dependencies":
                self.dependencies,

            "side_effects":
                self.side_effects,

            "complexity":
                self.complexity

        }



class ImpactAnalyzer:


    def analyze(
        self,
        project,
        target
    ):


        report = ImpactReport(
            target=target
        )


        if project is None:

            return report



        for package in project.packages:

            for file in package.files:

                for function in file.symbols:


                    if function.name == target:


                        report.calls.extend(
                            [
                                call.split("(")[0]
                                for call in function.calls
                            ]
                        )


                        report.dependencies.extend(
                            [
                                item.name
                                for item in function.dependencies
                            ]
                        )


                        report.side_effects.extend(
                            [
                                item.expression
                                for item in function.side_effects
                            ]
                        )



                    if target in function.calls:


                        report.callers.append(
                            function.name
                        )



        report.callers = list(
            set(report.callers)
        )


        report.calls = list(
            set(report.calls)
        )


        report.dependencies = list(
            set(report.dependencies)
        )


        report.side_effects = list(
            set(report.side_effects)
        )


        return report