from pathlib import Path
import re



class KnowledgeRepository:


    def __init__(
        self,
        base_path
    ):

        self.base_path = Path(
            base_path
        )



    def load(
        self,
        project_name
    ):


        project_path = (

            self.base_path

            /

            project_name

        )


        project_file = (

            project_path

            /

            "Project.md"

        )



        if not project_file.exists():

            return None



        content = project_file.read_text(
            encoding="utf-8"
        )


        return {

            "name":

                project_name,

            "functions":

                self._extract_section_items(
                    content,
                    "Functions"
                ),

            "files":

                self._extract_section_items(
                    content,
                    "Files"
                ),

            "packages":

                self._extract_section_items(
                    content,
                    "Packages"
                )

        }



    def load_project(
        self,
        project_name
    ):


        from .project_adapter import KnowledgeProjectAdapter


        data = self.load(
            project_name
        )


        if data is None:

            return None



        return KnowledgeProjectAdapter().from_dict(
            data
        )



    def search(
        self,
        query
    ):


        query = query.lower()



        results = []



        if not self.base_path.exists():

            return results



        for file in self.base_path.rglob(
            "*.md"
        ):


            content = file.read_text(
                encoding="utf-8"
            )


            score = self._score(
                query,
                content
            )



            if score > 0:


                results.append(

                    {

                        "file":

                            str(file),


                        "score":

                            score,


                        "content":

                            content

                    }

                )



        results.sort(

            key=lambda item:
                item["score"],

            reverse=True

        )


        return results



    def _score(
        self,
        query,
        content
    ):


        text = content.lower()


        words = query.split()


        score = 0



        for word in words:


            occurrences = len(

                re.findall(

                    r"\b"

                    +

                    re.escape(word)

                    +

                    r"\b",

                    text

                )

            )


            score += occurrences



        return score



    def _extract_section_items(
        self,
        content,
        section
    ):


        pattern = (

            r"## "

            +

            re.escape(section)

            +

            r"\n(.*?)(?=\n## |\Z)"

        )


        match = re.search(
            pattern,
            content,
            re.DOTALL
        )


        if match is None:

            return []



        lines = match.group(1).splitlines()


        result = []



        for line in lines:


            line = line.strip()



            if line.startswith("-"):

                result.append(

                    line[1:].strip()

                )



        return result