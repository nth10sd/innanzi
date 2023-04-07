"""Tests for start.py"""

from __future__ import annotations

from logging import INFO as INFO_LOG_LEVEL

import pytest

from innanzi import start


def test_main(caplog: pytest.LogCaptureFixture) -> None:
    """Test the main() function.

    :param caplog: Fixture to capture output logs
    """
    with caplog.at_level(INFO_LOG_LEVEL):
        start.RUN_LOG.propagate = True
        start.main()

        for entry in caplog.records:
            assert ": " in entry.message  # Test there is desired output
            if "Canada:" in entry.message:
                # Test that the output percentages are not zero
                assert float(entry.message.split()[-1].removesuffix("%"))
