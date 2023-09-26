import pytest
import logging
import pandas as pd

from geocollector.cli import Arguments, parse_args

test_csv_content = """#header
GSM,cell_type
GSM4952483,baso
"""


def test_parse_args_required_arguments():
    # Test with required arguments only
    argv = ["-i", "test.csv"]
    args = parse_args(argv)
    
    assert args.input_file == "test.csv"
    assert args.api_key == ""
    assert args.verbosity == logging.INFO


def test_parse_args_optional_arguments():
    # Test with optional arguments
    argv = ["-i", "test.csv", "-k", "your_api_key", "-v"]
    args = parse_args(argv)
    
    assert args.input_file == "test.csv"
    assert args.api_key == "your_api_key"
    assert args.verbosity == logging.DEBUG


def test_parse_args_verbosity_quiet():
    # Test verbosity option: quiet
    argv = ["-i", "test.csv", "-q"]
    args = parse_args(argv)
    
    assert args.input_file == "test.csv"
    assert args.api_key == ""
    assert args.verbosity == logging.ERROR
