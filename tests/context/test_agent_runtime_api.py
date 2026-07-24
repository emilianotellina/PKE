from pke.agent.api import AgentAPI

from pke.csr.graph import CSRGraph
from pke.csr.node import CSRNode
from pke.csr.relation import RelationType



def create_project():

    graph = CSRGraph()


    project = CSRNode(
        type="project",
        name="test_project"
    )


    package = CSRNode(
        type="package",
        name="test_package"
    )


    file = CSRNode(
        type="file",
        name="auth.py"
    )


    function = CSRNode(
        type="function",
        name="login"
    )


    graph.add(project)
    graph.add(package)
    graph.add(file)
    graph.add(function)


    graph.link(
        project,
        package,
        RelationType.CONTAINS
    )


    graph.link(
        package,
        file,
        RelationType.CONTAINS
    )


    graph.link(
        file,
        function,
        RelationType.DEFINES
    )


    return graph



def test_agent_api_selects_debug_agent():


    api = AgentAPI(
        create_project()
    )


    response = api.query(
        "fix login bug"
    )


    assert response.agent == "debug"

    assert response.profile == "debug"



def test_agent_api_selects_security_agent():


    api = AgentAPI(
        create_project()
    )


    response = api.query(
        "security audit authentication"
    )


    assert response.agent == "security"

    assert response.profile == "security"



def test_agent_api_exposes_agent_profile():


    api = AgentAPI(
        create_project()
    )


    response = api.query(
        "fix login bug"
    )


    assert response.agent == "debug"

    assert response.profile == "debug"



def test_agent_api_json_contains_agent_profile():


    api = AgentAPI(
        create_project()
    )


    data = api.query_json(
        "security audit authentication"
    )


    assert '"agent": "security"' in data

    assert '"profile": "security"' in data
    
def test_agent_api_debug_agent_applies_debug_profile():

    api = AgentAPI(
        create_project()
    )


    response = api.query(
        "fix login bug"
    )


    assert response.agent == "debug"

    assert response.profile == "debug"



def test_agent_api_security_agent_applies_security_profile():

    api = AgentAPI(
        create_project()
    )


    response = api.query(
        "security audit authentication"
    )


    assert response.agent == "security"

    assert response.profile == "security"