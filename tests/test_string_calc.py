from src.string_calc import StringCalc
import pytest

class TestStringCalc:


    def test_add_empty_string_returns_null(self):

        # Arrange
        string_calc = StringCalc()

        # Act
        result = string_calc.add("")

        # Assert
        assert result == 0


    def test_add_two_numbers(self):

        # Arrange
        string_calc = StringCalc()

        # Act
        result = string_calc.add("1,2")

        # Assert
        assert result == 3

    def test_add_three_numbers(self):

        # Arrange
        string_calc = StringCalc()

        # Act
        result = string_calc.add("1,2,1")

        # Assert
        assert result == 4

    def test_add_handles_new_lines_chars(self):

        # Arrange
        string_calc = StringCalc()

        # Act
        result = string_calc.add("1\n2, 3")

        # Assert
        assert result == 6

    def test_add_handles_new_lines_and_comma_bad_input(self):

        # Arrange
        string_calc = StringCalc()

        # Act
        result = string_calc.add("1,\n")

        # Assert
        assert result == 1


    def test_add_input_delimiters(self):

        # Arrange
        string_calc = StringCalc()

        # Act
        result = string_calc.add("//;\n1;2")

        # Assert
        assert result == 3

    def test_add_negatives_throw_an_exception(self):

        # Arrange
        string_calc = StringCalc()

        # Act / Assert
        try:
            result = string_calc.add("1,-2")
        except Exception:
            assert True
        else:
            assert False
