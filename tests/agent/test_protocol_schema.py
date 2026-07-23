from pke.agent.protocol_schema import ProtocolSchemaValidator



def test_protocol_schema_valid():


    validator = ProtocolSchemaValidator()



    payload = {

        "protocol_version": "1.0",

        "task": "analizza login",

        "target": "login",

        "context": {},

        "candidates": []

    }



    assert validator.validate(
        payload
    )



def test_protocol_schema_missing_fields():


    validator = ProtocolSchemaValidator()



    payload = {

        "protocol_version": "1.0",

        "task": "analizza login"

    }



    assert not validator.validate(
        payload
    )