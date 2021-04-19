"""Tests for common.py"""

from __future__ import annotations

from innanzi.common import LOSDevice


def test_losdevice() -> None:
    """Test the LOSDevice class."""
    device = LOSDevice("NewType")
    assert device.new_type == "NewType"
    assert device.compile() == "FOO"
