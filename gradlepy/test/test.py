import os
from unittest import TestCase

from gradlepy.run import Gradle

_DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')


class Test(TestCase):
  def test_gradle_run(self):
    gradle = Gradle()
    gradle.debug = True
    gradle.run_in_dir(_DATA_DIR)
