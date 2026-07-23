from dataclasses import dataclass


@dataclass
class QueryCandidate:


    symbol: str

    score: float


    def to_dict(self):

        return {

            "symbol":
                self.symbol,

            "score":
                self.score

        }