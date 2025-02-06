from src.class_under_test import ClassUnderTest
import pytest

class TestClassUnderTest:

    def test_simple(self):
        """ Test get_sprints"""

        # Arrange
        class_under_test = ClassUnderTest()

        # Act
        result = class_under_test.method_under_test()

        # Assert
        assert result == 1