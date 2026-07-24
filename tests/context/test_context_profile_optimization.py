from pke.context.context_profile import ContextProfile
from pke.context.token_optimizer import TokenOptimizer
from pke.context.optimized_context import OptimizedContext



class FakeSymbol:


    def __init__(
        self,
        name
    ):

        self.name = name



def test_profile_changes_compression():


    ranked = [

        (
            FakeSymbol("login"),
            100
        ),

        (
            FakeSymbol("database"),
            80
        )

    ]



    profile = ContextProfile(

        compression_mode="minimal"

    )



    result = TokenOptimizer().optimize(

        ranked,

        "login",

        10,

        profile

    )


    assert isinstance(

        result,

        OptimizedContext

    )



def test_profile_high_detail_formatter():


    from pke.context.context_formatter import ContextFormatter


    context = OptimizedContext(

        target="login"

    )


    context.add_symbol(
        "login",
        100
    )


    context.token_count = 5



    profile = ContextProfile(

        detail_level="high"

    )


    output = ContextFormatter().format_optimized(

        context,

        profile

    )


    assert "Token count" in output