from dataclasses import dataclass, field



@dataclass
class TaskIntent:


    action: str

    keywords: list[str] = field(
        default_factory=list
    )


    domain: str | None = None



class TaskIntentAnalyzer:



    ACTIONS = {

        "add": [
            "aggiungi",
            "crea",
            "implementa",
            "introduci",
            "add"
        ],

        "modify": [
            "modifica",
            "cambia",
            "aggiorna",
            "refactor",
            "update"
        ],

        "remove": [
            "rimuovi",
            "elimina",
            "delete"
        ],

        "analyze": [
            "analizza",
            "spiega",
            "descrivi",
            "analyze"
        ]

    }



    def analyze(
        self,
        task: str
    ):


        text = (
            task
            .lower()
            .replace("_", " ")
        )


        action = "analyze"


        for candidate, words in self.ACTIONS.items():

            for word in words:

                if word in text:

                    action = candidate

                    break



        keywords = [

            word

            for word in text.split()

            if len(word) > 3

        ]



        domain = None


        if (
            "auth" in text
            or "login" in text
            or "authentication" in text
        ):

            domain = "authentication"



        return TaskIntent(

            action=action,

            keywords=keywords,

            domain=domain

        )