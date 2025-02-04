# Copyright (c) Facebook, Inc. and its affiliates.
import unittest

import torcharrow.dtypes as dt
from torcharrow import Scope, IStringColumn

from .test_string_column import TestStringColumn


class TestStringColumnCpu(TestStringColumn):
    def setUp(self):
        self.device = "cpu"

    def test_empty(self):
        self.base_test_empty()

    def test_append_offsets(self):
        self.base_test_append_offsets()

    def test_comparision(self):
        return self.base_test_comparision()

    def test_concat(self):
        return self.base_test_concat()

    def test_string_split_methods(self):
        self.base_test_string_split_methods()

    def test_string_categorization_methods(self):
        return self.base_test_string_categorization_methods()

    def test_string_lifted_methods(self):
        self.base_test_string_lifted_methods()

    def test_string_pattern_matching_methods(self):
        return self.base_test_string_pattern_matching_methods()

    def test_regular_expressions(self):
        self.base_test_regular_expressions()


if __name__ == "__main__":
    unittest.main()
