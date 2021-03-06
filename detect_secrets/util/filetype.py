import os
from enum import Enum


class FileType(Enum):
    CLS = 0
    EXAMPLE = 1
    GO = 2
    JAVA = 3
    JAVASCRIPT = 4
    PHP = 5
    OBJECTIVE_C = 6
    PYTHON = 7
    SWIFT = 8
    TERRAFORM = 9
    YAML = 10
    OTHER = 11


def determine_file_type(filename: str) -> FileType:
    _, file_extension = os.path.splitext(filename)
    return {
        '.cls': FileType.CLS,
        '.example': FileType.EXAMPLE,
        '.eyaml': FileType.YAML,
        '.go': FileType.GO,
        '.java': FileType.JAVA,
        '.js': FileType.JAVASCRIPT,
        '.m': FileType.OBJECTIVE_C,
        '.php': FileType.PHP,
        '.py': FileType.PYTHON,
        '.pyi': FileType.PYTHON,
        '.swift': FileType.SWIFT,
        '.tf': FileType.TERRAFORM,
        '.yaml': FileType.YAML,
        '.yml': FileType.YAML,
    }.get(file_extension, FileType.OTHER)
