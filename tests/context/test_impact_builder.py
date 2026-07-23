from types import SimpleNamespace

from pke.context.impact_builder import ImpactBuilder



def test_impact_builder_creates_call_relations():


    project = SimpleNamespace(

        functions=[

            SimpleNamespace(

                name="login",

                calls=[

                    "authenticate()"

                ],

                dependencies=[]

            )

        ]

    )


    graph = ImpactBuilder().build(

        project

    )


    assert graph.contains(
        "login"
    )


    assert graph.get_relations(

        "login",

        "calls"

    ) == [

        "authenticate"

    ]



def test_impact_builder_creates_reverse_relations():


    project = SimpleNamespace(

        functions=[

            SimpleNamespace(

                name="login",

                calls=[

                    "authenticate()"

                ],

                dependencies=[]

            )

        ]

    )


    graph = ImpactBuilder().build(

        project

    )


    assert graph.get_relations(

        "authenticate",

        "called_by"

    ) == [

        "login"

    ]