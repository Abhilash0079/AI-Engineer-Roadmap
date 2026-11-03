import pytest
from text_preprocessing import preprocess_text

def test_preprocess_text_lowercase():
    result = preprocess_text("THIS MOVIE WAS AMAZING")

    assert result == "this movie was amazing"

def test_preprocess_text_removes_html():
    result = preprocess_text("This movie<br />was great!")
    
    assert result == "this movie was great"

def test_preprocess_text_preserves_negation():
    result = preprocess_text("This movie was not good")

    assert "not" in result

def test_preprocess_text_empty_input():
    with pytest.raises(ValueError, match="Review cannot be empty."):
        preprocess_text("")

def test_preprocess_text_non_string_input():
    with pytest.raises(TypeError, match="Review must be a string."):
        preprocess_text(123)

def test_preprocess_text_remove_extra_spaces():
    result = preprocess_text("  This   movie   was   great  ")

    assert result == "this movie was great"