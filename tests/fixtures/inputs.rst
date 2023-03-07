Inputs
======

Directives
----------

.. gql:input:: input1

    input1 tests parsing the simplest possible input definition

    .. gql:input:field:: field1: Float

        input1.field1 tests parsing the simplest possible input field definition

.. gql:input:: input2 @deprecated

    input2 tests that directives are parsed

    .. gql:input:field:: field1: Int @deprecated

        input2.field1 tests that directives are parsed

    .. gql:input:field:: field2: String = "defaultvaluefield2"

        input2.field2 tests that default values are parsed


Roles
-----

:gql:input:`input1`

:gql:input:field:`input1.field1`
