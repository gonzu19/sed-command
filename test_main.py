from main import substitute


def test_substitute() -> None:
    test_phrase = ["this is that"]
    expected_output = ["that is that"]
    assert substitute(array=test_phrase,
                      regex="s/this/that/g") == expected_output
