import os
import pathlib
import re
import shutil

import bs4
import pytest
from sphinx.application import Sphinx


def rebuild(**kwargs) -> None:
    """Build the documentation.

    Documentation is output to ``./_build/html``.
    """
    app = Sphinx(
        srcdir=".",
        confdir=".",
        outdir="_build/html",
        doctreedir="_build/.doctrees",
        buildername="html",
        warningiserror=True,
        confoverrides={"suppress_warnings": ["app"]},
        **kwargs,
    )
    app.build()


@pytest.fixture(scope="class")
def builder(tmp_path_factory):
    cwd = pathlib.Path.cwd()

    def build(test_name, **kwargs):
        dest = tmp_path_factory.mktemp(test_name)
        test_file = pathlib.Path("tests") / "fixtures" / f"{test_name}.rst"
        shutil.copy(test_file, dest / "index.rst")
        shutil.copy(pathlib.Path("tests") / "fixtures" / "conf.py", dest)
        os.chdir(dest)
        rebuild(**kwargs)

    yield build

    os.chdir(cwd)


def signature_text(soup: bs4.BeautifulSoup):
    # Strip the anchor character off the end
    result = soup.get_text()[:-1]
    # Strip the leading newline character that doesn't get displayed to users
    result = result.strip()
    # Condense double spaces created by HTML output quirks or `.get_text()` quirks
    result = re.sub("  ", " ", result)
    return result


class TestArguments:
    @pytest.fixture(scope="class")
    def soup(self, builder):
        builder("arguments")
        with (pathlib.Path("_build") / "html" / "index.html").open() as in_f:
            return bs4.BeautifulSoup(in_f, "html.parser")

    def test_multiple_arguments(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="fieldA1")
        assert signature_text(sig) == "fieldA1(arg1: type1, arg2: TestType): String"

    def test_argument_fields(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="fieldA1")
        links = sig.parent.find("ul").find_all("li")
        assert len(links) == 2
        enum_link, value_link = links
        assert enum_link.get_text().startswith("arg1")
        assert value_link.get_text().startswith("arg2")

    def test_type_is_linked(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="fieldA1")
        link = sig.a
        assert link, "Argument type did not resolve to a valid hyperlink"
        assert link.get_text() == "TestType"

    def test_with_directive(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="fieldB1")
        assert signature_text(sig) == "fieldB1(arg1: type1 @directiveA1): String"

    def test_with_directive_const_arguments(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="fieldB2")
        assert (
            signature_text(sig)
            == "fieldB2(arg1: type1 @directiveA1(arg1: 1, arg2: 2)): String"
        )

    def test_directive_is_linked(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="fieldB1")
        link = sig.a
        assert link, "Argument directive did not resolve to a valid hyperlink"
        assert link.get_text() == "directiveA1"

    def test_with_default_int_value(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="fieldC1")
        assert signature_text(sig) == "fieldC1(arg1: type1 = 600): String"

    def test_with_default_float_value(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="fieldC2")
        assert signature_text(sig) == "fieldC2(arg1: type1 = 1.5): String"

    def test_with_default_string_value(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="fieldC3")
        assert signature_text(sig) == 'fieldC3(arg1: type1 = "mystring"): String'

    def test_with_default_boolean_value(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="fieldC4")
        assert signature_text(sig) == "fieldC4(arg1: type1 = true): String"

    def test_with_default_null_value(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="fieldC5")
        assert signature_text(sig) == "fieldC5(arg1: type1 = null): String"

    def test_with_default_enum_value(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="fieldC6")
        assert signature_text(sig) == "fieldC6(arg1: type1 = ENUMVALUE): String"

    def test_with_default_list_value(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="fieldC7")
        assert signature_text(sig) == "fieldC7(arg1: type1 = [1, 2]): String"

    def test_with_default_object_value(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="fieldC8")
        assert signature_text(sig) == "fieldC8(arg1: type1 = {one: 1, two: 2}): String"

    def test_with_list_type(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="fieldD1")
        assert signature_text(sig) == "fieldD1(arg1: [TestType]): String"
        link = sig.a
        assert link, "Nested type did not resolve to a valid hyperlink"
        assert link.get_text() == "TestType"

    def test_with_non_null_type(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="fieldD2")
        assert signature_text(sig) == "fieldD2(arg1: TestType!): String"
        link = sig.a
        assert link, "Non-null type did not resolve to a valid hyperlink"
        assert link.get_text() == "TestType"

    def test_with_list_type_non_null_values(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="fieldD3")
        assert signature_text(sig) == "fieldD3(arg1: [TestType!]): String"
        link = sig.a
        assert link, "Nested non-null type did not resolve to a valid hyperlink"
        assert link.get_text() == "TestType"


class TestDirectives:
    @pytest.fixture(scope="class")
    def soup(self, builder):
        builder("directives")
        with (pathlib.Path("_build") / "html" / "index.html").open() as in_f:
            return bs4.BeautifulSoup(in_f, "html.parser")

    def test_simple_parse(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="directive1")
        assert signature_text(sig) == "directive @directive1 on SCHEMA"

    def test_multi_location(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="directive2")
        assert (
            signature_text(sig)
            == "directive @directive2 on FIELD_DEFINITION | ARGUMENT_DEFINITION"
        )

    def test_with_argument(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="directive3")
        assert signature_text(sig) == "directive @directive3(arg1: type1) on SCALAR"

        fields = sig.parent.find("ul").find_all("li")
        assert len(fields) == 1
        field = fields[0]
        assert field.get_text().startswith("arg1")

    def test_role(self, soup: bs4.BeautifulSoup):
        links = soup.find(id="roles").find_all("a", "reference")
        assert len(links) == 1
        link = links[0]
        assert link.get_text() == "directive1"


class TestEnums:
    @pytest.fixture(scope="class")
    def soup(self, builder):
        builder("enums")
        with (pathlib.Path("_build") / "html" / "index.html").open() as in_f:
            return bs4.BeautifulSoup(in_f, "html.parser")

    def test_simple_parse(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="enum1")
        assert signature_text(sig) == "enum enum1"

        sig = soup.find(id="enum1.value1")
        assert signature_text(sig) == "value1"

    def test_with_directive(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="enum2")
        assert signature_text(sig) == "enum enum2 @deprecated"

        sig = soup.find(id="enum2.value1")
        assert signature_text(sig) == "value1 @deprecated"

    def test_role(self, soup: bs4.BeautifulSoup):
        links = soup.find(id="roles").find_all("a", "reference")
        assert len(links) == 2
        enum_link, value_link = links
        assert enum_link.get_text() == "enum1"
        assert value_link.get_text() == "enum1.value1"


class TestInputs:
    @pytest.fixture(scope="class")
    def soup(self, builder):
        builder("inputs")
        with (pathlib.Path("_build") / "html" / "index.html").open() as in_f:
            return bs4.BeautifulSoup(in_f, "html.parser")

    def test_simple_parse(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="input1")
        assert signature_text(sig) == "input input1"

        sig = soup.find(id="input1.field1")
        assert signature_text(sig) == "field1: Float"

    def test_with_directive(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="input2")
        assert signature_text(sig) == "input input2 @deprecated"

        sig = soup.find(id="input2.field1")
        assert signature_text(sig) == "field1: Int @deprecated"

    def test_with_default_value(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="input2.field2")
        assert signature_text(sig) == 'field2: String = "defaultvaluefield2"'

    def test_role(self, soup: bs4.BeautifulSoup):
        links = soup.find(id="roles").find_all("a", "reference")
        assert len(links) == 2
        input_link, field_link = links
        assert input_link.get_text() == "input1"
        assert field_link.get_text() == "input1.field1"


class TestInterfaces:
    @pytest.fixture(scope="class")
    def soup(self, builder):
        builder("interfaces")
        with (pathlib.Path("_build") / "html" / "index.html").open() as in_f:
            return bs4.BeautifulSoup(in_f, "html.parser")

    def test_simple_parse(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="interface1")
        assert signature_text(sig) == "interface interface1"

        sig = soup.find(id="interface1.field1")
        assert signature_text(sig) == "field1: String"

    def test_with_directive(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="interface2")
        assert signature_text(sig) == "interface interface2 @deprecated"

        sig = soup.find(id="interface2.field1")
        assert signature_text(sig) == "field1: Int @deprecated"

    def test_with_default_value(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="interface2.field2")
        assert signature_text(sig) == "field2(arg1: Int = 0): String"

        fields = sig.parent.find("ul").find_all("li")
        assert len(fields) == 1
        field = fields[0]
        assert field.get_text().startswith("arg1")

    def test_role(self, soup: bs4.BeautifulSoup):
        links = soup.find(id="roles").find_all("a", "reference")
        assert len(links) == 2
        input_link, field_link = links
        assert input_link.get_text() == "interface1"
        assert field_link.get_text() == "interface1.field1"


class TestScalars:
    @pytest.fixture(scope="class")
    def soup(self, builder):
        builder("scalars")
        with (pathlib.Path("_build") / "html" / "index.html").open() as in_f:
            return bs4.BeautifulSoup(in_f, "html.parser")

    def test_simple_parse(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="scalar1")
        assert signature_text(sig) == "scalar scalar1"

    def test_with_directive(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="scalar2")
        assert signature_text(sig) == "scalar scalar2 @deprecated"

    def test_role(self, soup: bs4.BeautifulSoup):
        links = soup.find(id="roles").find_all("a", "reference")
        assert len(links) == 1
        link = links[0]
        assert link.get_text() == "scalar1"


class TestSchemas:
    @pytest.fixture(scope="class")
    def soup(self, builder):
        builder("schemas")
        with (pathlib.Path("_build") / "html" / "index.html").open() as in_f:
            return bs4.BeautifulSoup(in_f, "html.parser")

    def test_simple_parse(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="schema1")
        assert signature_text(sig) == "schema"

    def test_with_directive(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="schema2")
        assert signature_text(sig) == "schema @directive1 @directive2"

        fields = sig.parent.find("ul").find_all("li")
        assert len(fields) == 3
        query_field, mutation_field, subscription_field = fields
        assert query_field.get_text().startswith("query")
        assert query_field.find("a").get_text() == "MyQueryRootType1"
        assert mutation_field.get_text().startswith("mutation")
        assert mutation_field.find("a").get_text() == "MyMutationRootType1"
        assert subscription_field.get_text().startswith("subscription")
        assert subscription_field.find("a").get_text() == "MySubscriptionRootType1"

    def test_with_default_optypes(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="schema3")

        fields = sig.parent.find("ul").find_all("li")
        assert len(fields) == 3
        query_field, mutation_field, subscription_field = fields
        assert query_field.get_text().startswith("query")
        assert query_field.find("span").get_text() == "Query"
        assert mutation_field.get_text().startswith("mutation")
        assert mutation_field.find("span").get_text() == "Mutation"
        assert subscription_field.get_text().startswith("subscription")
        assert subscription_field.find("span").get_text() == "Subscription"

    def test_as_parent(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="schema4")

        type_sig = soup.find(id="schema4.MyQueryRootType2")
        assert signature_text(type_sig) == "type MyQueryRootType2"

        fields = sig.parent.find("ul").find_all("li")
        assert len(fields) == 2
        query_field, mutation_field = fields
        assert query_field.get_text().startswith("query")
        assert query_field.find("a").get_text() == "MyQueryRootType2"
        assert mutation_field.get_text().startswith("mutation")
        assert mutation_field.find("a").get_text() == "schema4.MyMutationRootType2"

    def test_role(self, soup: bs4.BeautifulSoup):
        links = soup.find(id="roles").find_all("a", "reference")
        assert len(links) == 1
        link = links[0]
        assert link.get_text() == "schema1"

    def test_role_resolution(self, soup: bs4.BeautifulSoup):
        links = soup.find(id="role-resolution").find_all("a", "reference")
        assert len(links) == 7
        default_roles = links[:4]
        assert all(role.get_text() == "MyType2" for role in default_roles)
        assert links[4].get_text() == "RoleType2"
        named_roles = links[5:]
        assert all(role.get_text() == "roleschema1.RoleType2" for role in named_roles)


class TestTypeObjects:
    @pytest.fixture(scope="class")
    def soup(self, builder):
        builder("type_objects")
        with (pathlib.Path("_build") / "html" / "index.html").open() as in_f:
            return bs4.BeautifulSoup(in_f, "html.parser")

    def test_simple_parse(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="type1")
        assert signature_text(sig) == "type type1"

        sig = soup.find(id="type1.field1")
        assert signature_text(sig) == "field1: Int"

    def test_with_directive(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="type2")
        assert signature_text(sig) == "type type2 @deprecated"

        sig = soup.find(id="type2.field1")
        assert signature_text(sig) == "field1: Int @deprecated"

    def test_with_default_value(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="type2.field2")
        assert signature_text(sig) == "field2(arg1: Int = 0): String"

        fields = sig.parent.find("ul").find_all("li")
        assert len(fields) == 1
        field = fields[0]
        assert field.get_text().startswith("arg1")

    def test_role(self, soup: bs4.BeautifulSoup):
        links = soup.find(id="roles").find_all("a", "reference")
        assert len(links) == 2
        input_link, field_link = links
        assert input_link.get_text() == "type1"
        assert field_link.get_text() == "type1.field1"


class TestUnions:
    @pytest.fixture(scope="class")
    def soup(self, builder):
        builder("unions")
        with (pathlib.Path("_build") / "html" / "index.html").open() as in_f:
            return bs4.BeautifulSoup(in_f, "html.parser")

    def test_simple_parse(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="union1")
        assert signature_text(sig) == "union union1 = Int"

    def test_with_multiple_member_types(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="union2")
        assert signature_text(sig) == "union union2 = union1 | String"

    def test_links_member_types(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="union2")
        link = sig.a
        assert link, "Nested type did not resolve to a valid hyperlink"
        assert link.get_text() == "union1"

    def test_with_directive(self, soup: bs4.BeautifulSoup):
        sig = soup.find(id="union3")
        assert signature_text(sig) == "union union3 @deprecated = Int"

    def test_role(self, soup: bs4.BeautifulSoup):
        links = soup.find(id="roles").find_all("a", "reference")
        assert len(links) == 1
        link = links[0]
        assert link.get_text() == "union1"
