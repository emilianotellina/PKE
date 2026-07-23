from .context_query import ContextQuery



def query(
    project,
    task,
    target=None,
    options=None,
    cache=None
):


    return ContextQuery(
        project,
        cache=cache
    ).execute(

        task=task,

        target=target,

        options=options

    )