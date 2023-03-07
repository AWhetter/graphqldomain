Enums
=====

Directives
----------

.. gql:enum:: enum1

    enum1 tests parsing the simplest possible enum definition

    .. gql:enum:value:: value1

        enum1.value1 tests parsing the simplest possible enum value definition

.. gql:enum:: enum2 @deprecated

    enum2 tests that directives are parsed

    .. gql:enum:value:: value1 @deprecated

        enum2.value1 tests that directives are parsed


Roles
-----

:gql:enum:`enum1`

:gql:enum:value:`enum1.value1`
