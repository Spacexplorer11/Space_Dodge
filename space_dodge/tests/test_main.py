import os
import sys

# Add the parent directory of tests (your root folder) to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import main


def test_main_runs():
    assert callable(main.main)
