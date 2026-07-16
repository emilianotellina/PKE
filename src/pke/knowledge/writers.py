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
        

    def write_package(
        self,
        package
    ):

        directory = (
            self.output /
            "packages" /
            package.name
        )


        directory.mkdir(
            parents=True,
            exist_ok=True
        )


        path = (
            directory /
            "Package.md"
        )


        path.write_text(
    f"""
    # Package: {package.name}


    ## Path

    {package.path}


    ## Files

    """ +
    "\n".join(
        f"- {f.name}"
        for f in package.files
    )
    )

    def write_file(
        self,
        file
    ):

        directory = (
            self.output /
            "files" /
            file.name
        )


        directory.mkdir(
            parents=True,
            exist_ok=True
        )


        path = (
            directory /
            "File.md"
        )


        path.write_text(
    f"""
    # File: {file.name}


    ## Path

    {file.path}


    ## Functions

    """ +
    "\n".join(
        f"- {f.name}"
        for f in file.functions
    )
    )