from pke.parser import PythonAdapter

from pke.knowledge import (
    KnowledgeCSRVisitor,
    CallResolver
)

from pke.csr.semantic_walker import SemanticWalker



source = """

def create_user(user):

    save_user(user)

    send_email(user)


def save_user(user):

    db.save(user)


def send_email(user):

    print(user)

"""



graph = PythonAdapter().parse(
    source
)



visitor = KnowledgeCSRVisitor(
    graph
)


walker = SemanticWalker(
    graph,
    visitor
)

walker.walk()



functions = (
    visitor
    .project
    .packages[0]
    .files[0]
    .symbols
)



resolver = CallResolver(
    functions
)



for function in functions:

    print(
        "\nFUNCTION:",
        function.name
    )


    for call in function.call_details:

        resolver.resolve(
            call
        )


        print(
            " ",
            call.caller,
            "->",
            call.target,
            "[",
            call.resolved_type,
            "]",
            call.module
        )