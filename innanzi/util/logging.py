"""Logging code."""

from __future__ import annotations

import logging
import sys


def get_logger(
    name: str,
    fmt: str = (
        "%(asctime)s %(name)-8s %(levelname)-8s {%(module)s} [%(funcName)s] %(message)s"
    ),
    filename: str = "",
    terminator: str = "\n",
) -> logging.Logger:
    """Create a logger, allowing setting filenames, output formats and line terminators.

    :param name: Name of logger
    :param fmt: Format of output message
    :param filename: Name of file to output the logs
    :param terminator: Line terminator (Use an empty string "" to log w/o line endings)
    :return: Desired logger object
    """
    logger = logging.getLogger(name)
    # If we use StreamHandler() without specifying sys.stdout, it defaults to sys.stderr
    # By using sys.stdout, stdout on console output should have both stdout & stderr
    c_handle = logging.StreamHandler(sys.stdout)
    c_handle.terminator = terminator
    c_handle.setFormatter(logging.Formatter(fmt=fmt, datefmt="%b %d %H:%M:%S"))
    logger.addHandler(c_handle)

    if filename:
        file_handler = logging.FileHandler(filename)
        file_handler.terminator = terminator
        file_handler.setFormatter(logging.Formatter(fmt=fmt, datefmt="%b %d %H:%M:%S"))
        logger.addHandler(file_handler)

    logger.propagate = False
    return logger
