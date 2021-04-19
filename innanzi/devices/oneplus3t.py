"""Code related to a OnePlus 3T."""

from __future__ import annotations

from innanzi.common import LOSDevice


class OP3TError(Exception):
    """Error class unique to OP3T objects."""


class OP3T(LOSDevice):
    """OnePlus 3T object."""

    def __init__(self) -> None:
        super().__init__("")

    # @classmethod
    # def main(cls) -> None:
    #     """Main function of OP3T class.
    #     """

    # @staticmethod
    # def compile() -> None:
    #     """Build a shell
    #     """
