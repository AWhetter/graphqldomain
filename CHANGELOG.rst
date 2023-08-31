graphqldomain v0.2.0 (2023-08-30)
=================================

Features
--------

- Added gql:schema directive (#1).

  Schemas and their operation types can be documented through the new directive.
  Other types can also be grouped under the schema and documented together.

  .. code-block:: rst

     .. gql:schema::

        :optype Query query:

        ..gql:type:: Query

           ...

        ...


Improved Documentation
----------------------

- Host documentation builds on readthedocs.


Misc
----

- Switched linter from pylint to ruff.
- Started testing in Python 3.12.


graphqldomain v0.1.0 (2023-03-17)
=================================

Features
--------

- Initial implementation.

  Included directives and roles for the following:

  - Directives
  - Enums and Enum Values
  - Inputs and Input Fields
  - Interfaces and Interface Fields
  - Scalars
  - Type Objects and Type Fields
  - Unions

  Added basic index generation. Supports parallel Sphinx builds.
