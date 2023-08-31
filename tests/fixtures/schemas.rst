Schemas
=======

Directives
----------

.. gql:type:: MyQueryRootType1

.. gql:type:: MyMutationRootType1

.. gql:type:: MySubscriptionRootType1

.. gql:schema::
    :name: schema1

    schema1 tests parsing the simplest possible schema definition

.. gql:schema:: @directive1 @directive2
    :name: schema2

    schema2 tests that directives are parsed, and operation types are rendered
    and linked.
    Note that these types are defined outside of the schema,
    because users may choose to document a schema without nesting all objects
    under the schema directive.

    :optype MyQueryRootType1 query:
    :optype MyMutationRootType1 mutation:
    :optype MySubscriptionRootType1 subscription:

.. gql:schema::
    :name: schema3

    schema3 tests that default operation names are used for operation types given without a name.

    :optype query:
    :optype mutation:
    :optype subscription:

.. gql:schema::
    :name: schema4

    schema4 tests that schema directives act as a part to child objects.
    Also that Operation Types link with or without specifying the schema name.

    :optype MyQueryRootType2 query:
    :optype schema4.MyMutationRootType2 mutation:

    .. gql:type:: MyQueryRootType2

    .. gql:type:: MyMutationRootType2


Roles
-----

:gql:schema:`schema1`


Role Resolution
---------------

.. gql:schema::

    .. gql:type:: MyType1

        This can link to :gql:type:`MyType2`
        or :gql:type:`__gqlschema__.MyType2`,
        but both are rendered the same.

    .. gql:type:: MyType2

This can link to :gql:type:`MyType2`
or :gql:type:`__gqlschema__.MyType2`,
but both are rendered the same.

.. gql:schema::
    :name: roleschema1

    .. gql:type:: RoleType1

        This can link to :gql:type:`RoleType2`
        or :gql:type:`roleschema1.RoleType2`.

    .. gql:type:: RoleType2

This can link to :gql:type:`roleschema1.RoleType2`
but cannot link to :gql:type:`RoleType2`.