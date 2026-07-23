from pke.agent.transport import AgentTransport
from pke.parser.python_adapter import PythonAdapter



def test_transport():


    project = PythonAdapter().parse(
        """
def login(user):

    return True
"""
    )


    transport = AgentTransport(
        project
    )


    response = transport.process(

        {
            "protocol_version": "1.0",

            "task": "analizza login",

            "target": "login"
        }

    )


    assert response.target == "login"



def test_transport_json():


    project = PythonAdapter().parse(
        """
def login(user):

    return True
"""
    )


    transport = AgentTransport(
        project
    )


    response = transport.process_json(

        {
            "task": "analizza login",

            "target": "login"
        }

    )


    assert isinstance(
        response,
        str
    )


    assert "protocol_version" in response