Type Objects
============

Directives
----------

.. gql:type:: type1

    type1 tests parsing the simplest possible type definition

    .. gql:type:field:: field1: Int

        type1.field1 tests parsing the simplest possible type field definition

.. gql:type:: type2 @deprecated

    type2 tests that directives are parsed

    .. gql:type:field:: field1: Int @deprecated

        type2.field1 tests that directives are parsed

    .. gql:type:field:: field2(arg1: Int = 0): String

        type2.field2 tests that arguments are parsed

        :argument arg1: arg1 tests that arguments can be documented.


Roles
-----

:gql:type:`type1`

:gql:type:field:`type1.field1`
