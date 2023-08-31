Added gql:schema directive.

Schemas and their operation types can be documented through the new directive.
Other types can also be grouped under the schema and documented together.

.. code-block:: rst

   .. gql:schema::

      :optype Query query:

      ..gql:type:: Query

         ...

      ...
