from pathlib import Path



class MarkdownWriter:


    def __init__(
        self,
        output
    ):

        self.output = Path(
            output
        )


        self.output.mkdir(
            exist_ok=True
        )



    def write_function(
        self,
        function
    ):

        path = (
            self.output /
            f"Function-{function.name}.md"
        )


        content = f"""
        # Function: {function.name}

        ## Signature

        {function.signature}

        ## Pseudocode


        {function.pseudocode}

        """


        path.write_text(
            content
        )
        