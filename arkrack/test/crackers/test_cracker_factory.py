import os
import unittest

from arkrack.crackers import cracker_factory


class TestCrackerFactory(unittest.TestCase):

  def setUp(self):
    self._factory = cracker_factory.CrackerFactory()

  def test_non_existing_file(self):
    self.assertFalse(self._factory.get_cracker('non.existing.file'))

  def test_zip_non_existing(self):
    self.assertFalse(self._factory.get_cracker('test.zip'))

  def test_zip(self):
    test_zip = os.path.join(os.path.dirname(os.path.abspath(__file__)),
        'testdata', 'testzip.zip')
    self.assertTrue(self._factory.get_cracker(test_zip))
