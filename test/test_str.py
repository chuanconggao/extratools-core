import pytest

from extratools_core.str import common_substr, enumerate_substrs, str_to_grams


def test_str_to_grams() -> None:
    assert list(str_to_grams("abc", n=1)) == ["a", "b", "c"]
    assert list(str_to_grams("abc", n=1, pad="_")) == ["a", "b", "c"]

    assert list(str_to_grams("abc", n=2)) == ["ab", "bc"]
    assert list(str_to_grams("abc", n=2, pad="_")) == ["_a", "ab", "bc", "c_"]

    assert list(str_to_grams("abc", n=3)) == ["abc"]
    assert list(str_to_grams("abc", n=3, pad="_")) == ["__a", "_ab", "abc", "bc_", "c__"]

    assert list(str_to_grams("abc", n=4)) == []

    with pytest.raises(ValueError):
        list(str_to_grams("abc", n=0))

    with pytest.raises(ValueError):
        list(str_to_grams("abc", n=2, pad="__"))


def test_common_substr() -> None:
    assert common_substr("abc", "abc") == "abc"
    assert common_substr("abc", "bcd") == "bc"
    assert common_substr("abc", "abcd") == "abc"
    assert not common_substr("", "")
    assert not common_substr("", "abc")
    assert not common_substr("abc", "def")


def test_enumerate_substrs() -> None:
    assert list(enumerate_substrs("")) == []

    assert list(enumerate_substrs("abc")) == [
        "a",
        "ab",
        "b",
        "bc",
        "c",
    ]

    assert list(enumerate_substrs("aaa")) == [
        "a",
        "aa",
        "a",
        "aa",
        "a",
    ]
