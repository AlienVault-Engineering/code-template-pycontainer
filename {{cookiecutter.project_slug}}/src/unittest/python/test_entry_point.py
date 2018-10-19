import os
import unittest

from {{cookiecutter.package_name}} import EntryPoint

ROOT_PATH = os.path.dirname(__file__)


class TestEntryPoint(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_execute_main_it_passes(self):
        EntryPoint.execute_main()
        self.assertEqual(True, True, "Woah!")
