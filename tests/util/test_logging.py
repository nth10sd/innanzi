"""Test logging.py."""

from __future__ import annotations

import filecmp
from logging import INFO
from pathlib import Path
import platform
from tempfile import NamedTemporaryFile

from innanzi.util.logging import get_logger


def test_get_logger(tmp_path: Path) -> None:
    """Test the get_logger function.

    :param tmp_path: Temp dir to test creation of a log file
    """
    log_name = "test_log"
    log_path = tmp_path / f"{log_name}.txt"
    logger = get_logger(
        log_name,
        fmt="%(name)-8s %(levelname)-8s {%(module)s} [%(funcName)s] %(message)s",
        filename=str(log_path),
        terminator=" different_terminator\n",
    )
    logger.setLevel(INFO)
    logger.error("This is a test error message")
    logger.info("This is a test info message")

    log_sample = Path(__file__).parents[1] / "data" / "log-sample.txt"
    # Terminator on Windows seems hardcoded to CRLF
    if platform.system() == "Windows":
        with log_path.open("rb") as f:
            new_content = f.read().replace(b"\r\n", b"\n")
        with log_path.open("wb") as f:
            f.write(new_content)

        with NamedTemporaryFile(
            delete=False, mode="w", newline="\n"
        ) as f, log_sample.open(encoding="utf-8", errors="surrogateescape") as g:
            f.writelines(g.readlines())
            log_sample = Path(f.name)  # Hash checksums are for LF line endings

    assert filecmp.cmp(
        log_path, log_sample
    ), "generated and expected output are not identical"
