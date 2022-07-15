
import unittest

from pyzipper import zipper

class TestPatterns(unittest.TestCase):
    def test_exclude_with_include(self):
        exclude_patterns = ["*.ignore"]
        include_patterns = ["*.include.ignore"]
        cases = [
            ("foo.ignore", True),
            ("bar.hoge.ignore", True),
            ("foo.include.ignore", False),
            ("bar.include.ignore", False),
            ("hello.png", False)
        ]
        for name, expect in cases:
            with self.subTest(name=name):
                actual = zipper.is_exclude(name, include_patterns, exclude_patterns)
                self.assertEqual(expect, actual)

