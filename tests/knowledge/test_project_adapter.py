from pke.knowledge.project_adapter import KnowledgeProjectAdapter



def test_adapter_creates_project_from_repository_data():


    data = {

        "name":
            "test_project",

        "packages":
            [
                "core"
            ],

        "files":
            [
                "login.py"
            ],

        "functions":
            [
                "login"
            ]

    }



    adapter = KnowledgeProjectAdapter()


    project = adapter.from_dict(
        data
    )


    assert project.name == "test_project"

    assert len(project.packages) == 1

    assert len(project.packages[0].files) == 1

    assert len(project.packages[0].files[0].symbols) == 1

    assert (
        project.packages[0]
        .files[0]
        .symbols[0]
        .name
        ==
        "login"
    )