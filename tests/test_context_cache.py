from pke.agent.context_cache import ContextCache



def test_context_cache():


    cache = ContextCache()


    context = {
        "test": True
    }


    cache.put(

        "project1",

        "login",

        "authenticate",

        {},

        context

    )



    result = cache.get(

        "project1",

        "login",

        "authenticate",

        {}

    )



    assert result == context



def test_context_cache_clear():


    cache = ContextCache()



    cache.put(

        "project1",

        "task",

        "target",

        {},

        "value"

    )



    cache.clear()



    assert cache.get(

        "project1",

        "task",

        "target",

        {}

    ) is None