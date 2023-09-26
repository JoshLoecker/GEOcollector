import logging

import pytest

from geocollector.logger import CustomFormatter, get_logger


@pytest.fixture
def formatter():
    return CustomFormatter()


def test_custom_formatter_format_info_message(formatter):
    record = logging.LogRecord(
        "test_logger",
        logging.INFO,
        "test.py",
        42,
        "This is an INFO message",
        (),
        None,
    )
    formatted_message = formatter.format(record)
    assert "\t\t" in formatted_message


def test_custom_formatter_format_other_message(formatter):
    record = logging.LogRecord(
        "test_logger",
        logging.DEBUG,
        "test.py",
        42,
        "This is an INFO message",
        (),
        None,
    )
    formatted_message = formatter.format(record)
    
    assert "\t" in formatted_message
    assert "\t\t" not in formatted_message


def test_get_logger():
    level = logging.DEBUG
    logger = get_logger(level)
    
    assert logger.level == level
    
    handler = logger.handlers[0]
    assert isinstance(handler, logging.StreamHandler)
    assert handler.level == level
    
    formatter = handler.formatter
    assert isinstance(formatter, CustomFormatter)
    assert formatter._style._fmt == "%(asctime)s - %(name)s:%(levelname)s\t\t%(message)s"
