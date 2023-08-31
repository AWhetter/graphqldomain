Directives
==========

Directives
----------

.. gql:directive:: @directive1 on SCHEMA

    directive1 tests parsing the simplest possible directive definition

.. gql:directive:: @directive2 on FIELD_DEFINITION | ARGUMENT_DEFINITION

    directive2 tests parsing with multiple type system directive locations

.. gql:directive:: @directive3(arg1: type1) on SCALAR

    directive3 tests that arguments are parsed

    :argument arg1: arg1 tests that arguments can be documented.


Roles
-----

:gql:directive:`directive1`
