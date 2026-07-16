from enum import Enum


class RelationType(str, Enum):

    CONTAINS = "CONTAINS"

    DEFINES = "DEFINES"

    IMPORTS = "IMPORTS"

    CALLS = "CALLS"

    EXTENDS = "EXTENDS"

    IMPLEMENTS = "IMPLEMENTS"

    BODY = "BODY"

    CONDITION = "CONDITION"

    THEN = "THEN"

    ELSE = "ELSE"

    VALUE = "VALUE"

    TARGET = "TARGET"

    ARGUMENT = "ARGUMENT"

    LEFT = "LEFT"

    RIGHT = "RIGHT"

    NEXT = "NEXT"

    PREVIOUS = "PREVIOUS"

    ITERABLE = "ITERABLE"

    EXCEPTION = "EXCEPTION"

    FINALLY = "FINALLY"

    OBJECT = "OBJECT"

    INDEX = "INDEX"

    KEY = "KEY"

    VALUE = "VALUE"

    ELEMENT = "ELEMENT"