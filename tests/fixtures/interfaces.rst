Interfaces
==========

Directives
----------

.. gql:interface:: interface1

    interface1 tests parsing the simplest possible interface definition

    .. gql:interface:field:: field1: String

        interface1.field1 tests parsing the simplest possible interface field definition

.. gql:interface:: interface2 @deprecated

    interface2 tests that directives are parsed

    .. gql:interface:field:: field1: Int @deprecated

        interface2.field1 tests that directives are parsed

    .. gql:interface:field:: field2(arg1: Int = 0): String

        interface2.field2 tests that arguments are parsed


Roles
-----

:gql:interface:`interface1`

:gql:interface:field:`interface1.field1`
