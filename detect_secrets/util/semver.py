"""
NOTE(2020-11-07|domanchi): We probably can use `python-semver` to do this. However, at the
time of writing, it doesn't look like it's ready for production. Therefore, this implements
a very basic version of it.
"""
from typing import Any


class Version:
    def __init__(self, version: str) -> None:
        self.major, self.minor, self.patch = map(int, version.split('.'))

    def __lt__(self, other: Any) -> bool:
        if not isinstance(other, Version):
            raise NotImplementedError

        if self.major < other.major:
            return True
        if self.major > other.major:
            return False

        if self.minor < other.minor:
            return True
        if self.minor > other.minor:
            return False

        if self.patch < other.patch:
            return True

        return False

    def __gt__(self, other: Any) -> bool:
        return not self.__lt__(other)

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Version):
            raise NotImplementedError

        return (
            self.major == other.major
            and self.minor == other.minor
            and self.patch == other.patch
        )

    def __le__(self, other: Any) -> bool:
        return self.__lt__(other) or self.__eq__(other)

    def __ge__(self, other: Any) -> bool:
        return self.__gt__(other) or self.__eq__(other)
