Unions
======

Directives
----------

.. gql:union:: union1 = Int

    union1 tests parsing the simplest possible union definition

.. gql:union:: union2 = union1 | String

    union2 tests parsing multiple union members types

.. gql:union:: union3 @deprecated = Int

    union3 tests that directives are parsed

Roles
-----

:gql:union:`union1`
