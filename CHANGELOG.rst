Changelog
=========

Versions follow `Semantic Versioning <https://semver.org/>`_ (``<major>.<minor>.<patch>``).

.. towncrier release notes start

v1.0.0 (2025-02-17)
-------------------

Features
^^^^^^^^

- Add support for Python 3.12 and 3.13


Misc
^^^^

- Drop support for Python 3.8
- Implemented automatic uploads to PyPI
- Switch from black and pylint to ruff
- Update development workflows to use Python 3.13


v0.2.0 (2023-08-30)
-------------------

Features
^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^

- Host documentation builds on readthedocs.


Misc
^^^^

- Switched linter from pylint to ruff.
- Started testing in Python 3.12.


v0.1.0 (2023-03-17)
-------------------

Features
^^^^^^^^

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
