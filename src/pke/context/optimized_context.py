from dataclasses import dataclass, field



@dataclass
class OptimizedContext:


    target: str


    symbols: list = field(
        default_factory=list
    )


    summary: str = ""



    token_count: int = 0



    def add_symbol(
        self,
        symbol,
        score
    ):


        self.symbols.append(

            {

                "symbol":
                    symbol,

                "score":
                    score

            }

        )



    def to_dict(
        self
    ):


        return {

            "target":
                self.target,

            "symbols":
                self.symbols,

            "summary":
                self.summary,

            "token_count":
                self.token_count

        }