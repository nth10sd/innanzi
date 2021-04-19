"""Code related to a OnePlus 6T."""

from __future__ import annotations

from innanzi.common import LOSDevice


class OP6TError(Exception):
    """Error class unique to OP6T objects."""


class OP6T(LOSDevice):
    """OnePlus 6T object."""

    def __init__(self) -> None:
        super().__init__("")

    # @classmethod
    # def main(cls) -> None:
    #     """Main function of OP6T class.
    #     """

    # @staticmethod
    # def compile() -> None:
    #     """Build a shell
    #     """
