"""import import to_roman_numeral() and to_arabic_number() from roman_numeral_converter.py"""
import pytest

from converter import to_roman_numeral, to_arabic_number


def test_given_when_then():
    # Given
    input_a = 1
    input_b = 1
    expected_output = 2
    # When
    output = input_a + input_b
    # Then
    assert output == expected_output

def test_given_when_then_fail():
    # Given
    input_a = 2
    input_b = 2
    expected_output = 5
    # When
    output = input_a + input_b
    # Then
    assert output == expected_output
