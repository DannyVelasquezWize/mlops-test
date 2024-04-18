import pytest
import os
import sys

sys.path.insert(
    0, os.getcwd()
)
sys.path.insert(
    0, os.path.join(os.getcwd(), "src")
)

pytest_plugins = ["test.fixtures.utils_fixtures"]
