from pke.context.context_item import ContextItem



class FakeSymbol:

    def __init__(
        self,
        name
    ):

        self.name = name

        self.type = "function"



def test_context_item_total_score():

    item = ContextItem(

        FakeSymbol("login"),

        graph_score=100,

        retrieval_score=20,

        risk_score=5

    )


    assert item.total_score() == 125



def test_context_item_update_score():

    item = ContextItem(

        FakeSymbol("login"),

        graph_score=80,

        retrieval_score=10

    )


    item.update_score()


    assert item.score == 90



def test_context_item_add_score():

    item = ContextItem(

        FakeSymbol("login")

    )


    item.add_score(

        "retrieval",

        30

    )


    item.add_score(

        "risk",

        10

    )


    assert item.retrieval_score == 30

    assert item.risk_score == 10

    assert item.score == 40



def test_context_item_to_dict():

    item = ContextItem(

        FakeSymbol("login"),

        graph_score=100

    )


    item.update_score()


    data = item.to_dict()


    assert data["symbol"] == "login"

    assert data["type"] == "function"

    assert data["score"] == 100