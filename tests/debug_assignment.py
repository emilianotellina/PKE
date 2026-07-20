from pke.parser.python_adapter import PythonAdapter
from pke.csr.relation import RelationType


def test_debug_assignment():

    graph = PythonAdapter().parse(
        """
def login(user):
    token = authenticate(user)
    return token
"""
    )


    assignments = graph.find(
        node_type="assignment"
    )


    assert len(assignments) == 1


    assignment = assignments[0]


    print("\nASSIGNMENT:", assignment)


    print(
        "TARGET:",
        graph.children(
            assignment,
            RelationType.TARGET
        )
    )


    print(
        "VALUE:",
        graph.children(
            assignment,
            RelationType.VALUE
        )
    )


    print(
        "LEFT:",
        graph.children(
            assignment,
            RelationType.LEFT
        )
    )


    print(
        "RIGHT:",
        graph.children(
            assignment,
            RelationType.RIGHT
        )
    )