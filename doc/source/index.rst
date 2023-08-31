:mod:`graphqldomain`
====================

This extension provides a Sphinx domain for describing GraphQL schemas.

In order to use this extension,
add :mod:`graphqldomain` to the :confval:`sphinx:extensions`
list in your :doc:`conf.py <sphinx:usage/configuration>` file.

.. code-block:: python

   extensions = ["graphqldomain"]


Directives
----------

.. rst:directive:: .. gql:directive:: definition

   Describes a GraphQL directive defined in a schema.

   The ``definition`` argument is the definition of the directive,
   using the format described in the GraphQL spec
   (https://spec.graphql.org/June2018/#sec-Type-System.Directives).
   However it should not include the following:

   * The ``Description``, which goes into the body of this directive.
   * The ``directive`` keyword.

   The ``:argument <name>: <description>`` field can be used to document the arguments
   (https://spec.graphql.org/June2018/#ArgumentsDefinition).

   For example:

   .. code-block:: rst

      .. gql:directive:: @slow(super: Boolean = false) on FIELD_DEFINITION | ARGUMENT_DEFINITION

         Indicates that the usage of this field or argument is slow,
         and therefore queries with this field or argument should be made sparingly.

         :argument super: Whether usage will be super slow, or just a bit slow.


   This will be rendered as:

      .. gql:directive:: @slow(super: Boolean = false) on FIELD_DEFINITION | ARGUMENT_DEFINITION

         Indicates that the usage of this field or argument is slow,
         and therefore queries with this field or argument should be made sparingly.

         :argument super: Whether usage will be super slow, or just a bit slow.

.. rst:directive:: .. gql:enum:: definition

   Describes a GraphQL enum defined in a schema.

   The ``definition`` argument is the definition of the enum,
   using the format described in the GraphQL spec
   (https://spec.graphql.org/June2018/#sec-Enums).
   However it should not include the following:

   * The ``Description``, which goes into the body of this directive.
   * The ``enum`` keyword.
   * The ``EnumValuesDefinition``. Enum values can be described with the
     :rst:dir:`gql:enum:value` directive.

   For example:

   .. code-block:: rst

      .. gql:enum:: CharacterCase

         The casing of a character.

   This will be rendered as:

      .. gql:enum:: CharacterCase

         The casing of a character.


.. rst:directive:: .. gql:enum:value:: definition

   Describes a GraphQL enum value defined on an enum in a schema.

   The ``definition`` argument is the definition of the enum value,
   using the format described in the GraphQL spec
   (https://spec.graphql.org/June2018/#EnumValueDefinition).
   However it should not include the following:

   * The ``Description``, which goes into the body of this directive.

   For example:

   .. code-block:: rst

      .. gql:enum:: CharacterCase

         The casing of a character.

         .. gql:enum:value:: UPPER

            Upper case.

         .. gql:enum:value:: LOWER

            Lower case.

   This will be rendered as:

      .. gql:enum:: CharacterCase

         The casing of a character.

         .. gql:enum:value:: UPPER

            Upper case.

         .. gql:enum:value:: LOWER

            Lower case.


.. rst:directive:: .. gql:input:: definition

   Describes a GraphQL input object defined in a schema.

   The ``definition`` argument is the definition of the input object,
   using the format described in the GraphQL spec
   (https://spec.graphql.org/June2018/#sec-Input-Objects).
   However it should not include the following:

   * The ``Description``, which goes into the body of this directive.
   * The ``input`` keyword.
   * The ``InputFieldDefinition``. Input values can be described with the
     :rst:dir:`gql:input:value` directive.

   For example:

   .. code-block:: rst

      .. gql:input:: Point2D

         A point in a 2D coordinate system.

   This will be rendered as:

   .. gql:input:: Point2D

      A point in a 2D coordinate system.


.. rst:directive:: .. gql:input:field:: definition

   Describes a GraphQL input field defined on an input in a schema.

   The ``definition`` argument is the definition of the input field,
   using the format described in the GraphQL spec
   (https://spec.graphql.org/June2018/#InputValueDefinition).
   However it should not include the following:

   * The ``Description``, which goes into the body of this directive.

   For example:

   .. code-block:: rst

      .. gql:input:: Point2D

         A point in a 2D coordinate system.

         .. gql:input:field:: x: Float

            The ``x`` coordinate of the point.

         .. gql:input:field:: y: Float

            The ``y`` coordinate of the point.

   This will be rendered as:

      .. gql:input:: Point2D

         A point in a 2D coordinate system.

         .. gql:input:field:: x: Float

            The ``x`` coordinate of the point.

         .. gql:input:field:: y: Float

            The ``y`` coordinate of the point.


.. rst:directive:: .. gql:interface:: definition

   Describes a GraphQL interface defined on a schema.

   The ``definition`` argument is the definition of the interface,
   using the format described in the GraphQL spec
   (https://spec.graphql.org/June2018/#sec-Interfaces).
   However it should not include the following:

   * The ``Description``, which goes into the body of this directive.
   * The ``interface`` keyword.
   * The ``FieldsDefinition``. Interface fields can be described with the
     :rst:dir:`gql:interface:field` directive.

   For example:

   .. code-block:: rst

      .. gql:interface:: NamedEntity

         An entity with a name.

   This will be rendered as:

      .. gql:interface:: NamedEntity

         An entity with a name.


.. rst:directive:: .. gql:interface:field:: definition

   Describes a GraphQL interface field defined on an interface in a schema.

   The ``definition`` argument is the definition of the interface field,
   using the format described in the GraphQL spec
   (https://spec.graphql.org/June2018/#FieldDefinition).
   However it should not include the following:

   * The ``Description``, which goes into the body of this directive.

   The ``:argument <name>: <description>`` field can be used to document the arguments
   (https://spec.graphql.org/June2018/#ArgumentsDefinition).

   For example:

   .. code-block:: rst

      .. gql:interface:: NamedEntity

         An entity with a name.

         .. gql:interface:field:: name(lower: Boolean = false): String

            The name of the entity.

            :argument lower: Whether to lowercase the name or not.

   This will be rendered as:

      .. gql:interface:: NamedEntity

         An entity with a name.

         .. gql:interface:field:: name(lower: Boolean = false): String

            The name of the entity.

            :argument lower: Whether to lowercase the name or not.


.. rst:directive:: .. gql:scalar:: definition

   Describes a GraphQL scalar type defined on a schema.

   The ``definition`` argument is the definition of the scalar type,
   using the format described in the GraphQL spec
   (https://spec.graphql.org/June2018/#sec-Scalars).
   However it should not include the following:

   * The ``Description``, which goes into the body of this directive.
   * The ``scalar`` keyword.

   For example:

   .. code-block:: rst

      .. gql:scalar:: Url

         A string that represents a valid URL.

   This will be rendered as:

      .. gql:scalar:: Url

         A string that represents a valid URL.


.. rst:directive:: .. gql:schema:: definition

   Describes a GraphQL schema.

   The ``definition`` argument is the definition of the schema,
   using the format described in the GraphQL spec
   (https://spec.graphql.org/June2018/#sec-Schema).
   However it should not include the following:

   * The ``schema`` keyword.
   * The ``RootOperationTypeDefinition``,
     which is documented via the ``optype`` field.

   In other words, you should only include the directives
   (https://spec.graphql.org/June2018/#Directives).


   The ``:optype <type> (query|mutation|subscription):`` field can be used to
   document the Root Operation Types
   (https://spec.graphql.org/June2018/#sec-Root-Operation-Types).
   If an ``optype`` field is specified without a type then it will
   default to the usual default Operation Types ``Query``, ``Mutation``,
   or ``Subscription``.

   .. rubric:: Options

   .. rst:directive:option:: name

      An arbitrary identifier given to the schema
      for use by Sphinx in cross-references and URLs to this schema.
      This can be useful for documenting multiple schemas in the same documentation,
      but isn't necessary when documenting a single schema.
      Defaults to ``__gqlschema__``.

   For example:

   .. code-block:: rst

      .. gql:schema:: @mydirective
         :name: myschema

         An example schema.

         :optype MyQueryType query:
         :optype mutation:
         :optype MySubscriptionType subscription:

         .. gql:type:: MyQueryType

            Types and other definitions are usually grouped under a schema.

         .. gql:directive:: @mydirective on SCHEMA

   This will be rendered as:

      .. gql:schema:: @mydirective
         :name: myschema

         An example schema.

         :optype MyQueryType query:
         :optype mutation:
         :optype MySubscriptionType subscription:

         .. gql:type:: MyQueryType

            Types and other definitions are usually grouped under a schema.

         .. gql:directive:: @mydirective on SCHEMA


.. rst:directive:: .. gql:type:: definition

   Describes a GraphQL object type defined on a schema.

   The ``definition`` argument is the definition of the object type,
   using the format described in the GraphQL spec
   (https://spec.graphql.org/June2018/#sec-Objects).
   However it should not include the following:

   * The ``Description``, which goes into the body of this directive.
   * The ``type`` keyword.
   * The ``FieldsDefinition``. Interface fields can be described with the
     :rst:dir:`gql:type:field` directive.

   For example:

   .. code-block:: rst

      .. gql:type:: Person implements NamedEntity

         A human person.

   This will be rendered as:

   .. gql:type:: Person implements NamedEntity

      A human person.


.. rst:directive:: .. gql:type:field:: definition

   Describes a GraphQL field defined on an object type in a schema.

   The ``definition`` argument is the definition of the type field,
   using the format described in the GraphQL spec
   (https://spec.graphql.org/June2018/#FieldDefinition).
   However it should not include the following:

   * The ``Description``, which goes into the body of this directive.
   * The ``type`` keyword.
   * The ``FieldsDefinition``. Interface fields can be described with the
     :rst:dir:`gql:interface:value` directive.

   The ``:argument <name>: <description>`` field can be used to document the arguments
   (https://spec.graphql.org/June2018/#ArgumentsDefinition).

   For example:

   .. code-block:: rst

      .. gql:type:: Person implements NamedEntity

         A human person.

         .. gql:type:field:: age: Int

            How old the person is in years.

         .. gql:type:field:: picture(format: String = "jpg"): Url

            :argument format: The desired file format of image.

   This will be rendered as:

      .. gql:type:: Person implements NamedEntity

         A human person.

         .. gql:type:field:: age: Int

            How old the person is in years.

         .. gql:type:field:: picture(format: String = "jpg"): Url

            :argument format: The desired file format of image.


.. rst:directive:: .. gql:union:: definition

   Describes a GraphQL union defined on a schema.

   The ``definition`` argument is the definition of the union,
   using the format described in the GraphQL spec
   (https://spec.graphql.org/June2018/#sec-Unions).
   However it should not include the following:

   * The ``Description``, which goes into the body of this directive.
   * The ``union`` keyword.

   For example:

   .. code-block:: rst

      .. gql:union:: Centre = Person | Point2D

         A possible centre of the universe.

   This will be rendered as:

      .. gql:union:: Centre = Person | Point2D

         A possible centre of the universe.


Roles
-----

All GraphQL directives have a role with the same name that can be used to
refer to those objects.
For example a GraphQL ``type`` defined with the :rst:dir:`gql:type` directive
can be referred to using the :rst:role:`gql:type` role.

.. rst:role:: gql:directive

   Refers to a GraphQL directive defined with the :rst:dir:`gql:directive` rST directive.

.. rst:role:: gql:enum

   Refers to a GraphQL enum defined with the :rst:dir:`gql:enum` rST directive.

.. rst:role:: gql:enum:value

   Refers to a GraphQL enum value defined with the :rst:dir:`gql:enum:value` rST directive.

.. rst:role:: gql:input

   Refers to a GraphQL input defined with the :rst:dir:`gql:input` rST directive.

.. rst:role:: gql:input:field

   Refers to a GraphQL input field defined with the :rst:dir:`gql:input:field` rST directive.

.. rst:role:: gql:interface

   Refers to a GraphQL interface defined with the :rst:dir:`gql:interface` rST directive.

.. rst:role:: gql:interface:field

   Refers to a GraphQL interface field defined with the :rst:dir:`gql:interface:field` rST directive.

.. rst:role:: gql:scalar

   Refers to a GraphQL scalar defined with the :rst:dir:`gql:scalar` rST directive.

.. rst:role:: gql:schema

   Refers to a GraphQL schema defined with the :rst:dir:`gql:schema` rST directive.

.. rst:role:: gql:type

   Refers to a GraphQL type defined with the :rst:dir:`gql:type` rST directive.

.. rst:role:: gql:type:field

   Refers to a GraphQL type field defined with the :rst:dir:`gql:type:field` rST directive.

.. rst:role:: gql:union

   Refers to a GraphQL union defined with the :rst:dir:`gql:union` rST directive.


Using Schema Names In Roles
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you are documenting a single schema and therefore choose not to use the
``:name:`` option to name your :rst:dir:`gql:schema`,
using the schema name in roles is never required.

For example:

.. code-block :: rst

   .. gql:schema::

      .. gql:type:: MyType1

         This can link to :gql:type:`MyType2`
         or :gql:type:`__gqlschema__.MyType2`,
         but both are rendered the same.

      .. gql:type:: MyType2

   This can link to :gql:type:`MyType2`
   or :gql:type:`__gqlschema__.MyType2`,
   but both are rendered the same.

This will be rendered as:

   .. gql:schema::

      .. gql:type:: MyType1

         This can link to :gql:type:`MyType2`
         or :gql:type:`__gqlschema__.MyType2`,
         but both are rendered the same.

      .. gql:type:: MyType2

   This can link to :gql:type:`MyType2`
   or :gql:type:`__gqlschema__.MyType2`,
   but both are rendered the same.


Advanced
^^^^^^^^

If you have more complex documentation that uses the
``:name:`` option to name one or more :rst:dir:`gql:schema` definitions,
then using the schema name in roles is often required to eliminate
a role ever having ambiguous targets
(e.g. if two schemas defined a ``MyType`` type, a :rst:role:`gql:type`
to ``MyType`` could link to the ``MyType`` type from either schema).

Roles used inside a schema definition can skip prepending the schema name.
Roles used outside a schema must prepend the schema name for named schemas.

For example:

.. code-block :: rst

   .. gql:schema::
      :name: roleschema1

      .. gql:type:: RoleType1

         This can link to :gql:type:`RoleType2`
         or :gql:type:`roleschema1.RoleType2`.

      .. gql:type:: RoleType2

   This can link to :gql:type:`roleschema1.RoleType2`
   but cannot link to :gql:type:`RoleType2`.

This will be rendered as:

   .. gql:schema::
      :name: roleschema1

      .. gql:type:: RoleType1

         This can link to :gql:type:`RoleType2`
         or :gql:type:`roleschema1.RoleType2`.

      .. gql:type:: RoleType2

   This can link to :gql:type:`roleschema1.RoleType2`
   but cannot link to :gql:type:`RoleType2`.