from pke.agent.prompt import AgentPrompt
from pke.context.prompt_document import PromptDocument



def test_agent_prompt():


    document = PromptDocument()


    document.add_section(
        "Context",
        "Function login"
    )



    prompt = AgentPrompt(

        task="modifica login",

        target="login",

        document=document

    )



    result = prompt.to_text()



    assert "Function login" in result

    assert "Context" in result