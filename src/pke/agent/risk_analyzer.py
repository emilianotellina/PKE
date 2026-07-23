class RiskAnalyzer:


    def analyze(
        self,
        project,
        target,
        metrics=None
    ):

        risks = []


        if metrics is None:

            return risks


        function_metrics = metrics.get(
            target,
            {}
        )


        fan_out = function_metrics.get(
            "fan_out",
            0
        )


        complexity = function_metrics.get(
            "complexity",
            0
        )


        criticality = function_metrics.get(
            "criticality",
            0
        )


        instability = function_metrics.get(
            "instability",
            0
        )


        if fan_out > 5:

            risks.append(
                "high fan-out function"
            )


        if complexity > 10:

            risks.append(
                "high complexity function"
            )


        if criticality > 7:

            risks.append(
                "critical function"
            )


        if instability > 0.7:

            risks.append(
                "unstable dependency"
            )


        return risks