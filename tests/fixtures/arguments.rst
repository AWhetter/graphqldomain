Arguments
=========

Tests for complex argument parsing

.. gql:type:: TestType

.. gql:directive:: @directiveA1 on ARGUMENT_DEFINITION

.. gql:type:field:: fieldA1(name1: type1, name2: TestType): String

    fieldA1 tests parsing with multiple arguments

    :argument name1: name1 tests that arguments can be documented.
    :argument name2: name2 tests that arguments can be documented.

.. gql:type:field:: fieldB1(name1: type1 @directiveA1): String

    fieldB1 tests parsing with an argument directive

.. gql:type:field:: fieldB2(name1: type1 @directiveA1(name1: 1, name2: 2)): String

    fieldB2 tests parsing with an argument directive that has const arguments

.. gql:type:field:: fieldC1(name1: type1 = 600): String

    fieldC1 tests parsing with an argument that has a default integer value

.. gql:type:field:: fieldC2(name1: type1 = 1.5): String

    fieldC2 tests parsing with an argument that has a default float value

.. gql:type:field:: fieldC3(name1: type1 = "mystring"): String

    fieldC3 tests parsing with an argument that has a default string value

.. gql:type:field:: fieldC4(name1: type1 = true): String

    fieldC4 tests parsing with an argument that has a default boolean value

.. gql:type:field:: fieldC5(name1: type1 = null): String

    fieldC5 tests parsing with an argument that has a default null value

.. gql:type:field:: fieldC6(name1: type1 = ENUMVALUE): String

    fieldC6 tests parsing with an argument that has a default enum value

.. gql:type:field:: fieldC7(name1: type1 = [1, 2]): String

    fieldC7 tests parsing with an argument that has a default list value

.. gql:type:field:: fieldC8(name1: type1 = {one: 1, two: 2}): String

    fieldC8 tests parsing with an argument that has a default object value

.. gql:type:field:: fieldD1(name1: [TestType]): String

    fieldD1 tests parsing with an argument that has a list type

.. gql:type:field:: fieldD2(name1: TestType!): String

    fieldD2 tests parsing with an argument that has a list type

.. gql:type:field:: fieldD3(name1: [TestType!]): String

    fieldD3 tests parsing with an argument that has a list type with non-null values
