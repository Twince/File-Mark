from typing import Union

from .file import File, Directory

FileOrDirectory = Union[File, Directory]

__all__ = ("File", "Directory", "FileOrDirectory")
